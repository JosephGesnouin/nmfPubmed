####Libraries#####
library(readr)
library(Matrix)
library(NMF)
library(tidytext)
library(tm)
library(slam)
library(dplyr)
library(SnowballC)
library(skmeans)
library(textir)
library(stm)
library(factoextra)
library(foreach)
library(doParallel)
library(fastICA)
library(wordcloud)
library(topicmodels)


###importation des données + remplacement valeurs abérantes et création de matrices####
brute <- read_csv("~/Documents/PROJET/Matrices/brute.csv", 
                  col_names = FALSE)
brute$X3[is.na(brute$X3)] <- 1
x1 <- as.factor(brute$X1)
levels(x1) <- 1:length(levels(x1))
x1 <- as.numeric(x1)

x2 <- as.factor(brute$X2)
levels(x2) <- 1:length(levels(x2))
x2 <- as.numeric(x2)

dicMaladies=sort(unique(brute$X1))
dicGenes=sort(unique(brute$X2))
data_stm=simple_triplet_matrix(x1, x2, brute$X3, nrow = max(x1), ncol = max(x2),dimnames =list(dicMaladies,dicGenes))
data=matrix(data_stm,nrow=length(dicMaladies),ncol=length(dicGenes),dimnames =list(dicMaladies,dicGenes) )
data_sparse=Matrix(data, sparse=TRUE)

####Création de la matrice que l'on va utiliser pour les normalisation Genes par maladies: 16000x4000####
Data_stm_GpM=simple_triplet_matrix(x2,x1,brute$X3,nrow=max(x2),ncol=max(x1),dimnames=list(dicGenes,dicMaladies))
data_GpM=matrix(Data_stm_GpM,nrow=length(dicGenes),ncol=length(dicMaladies),dimnames=list(dicGenes,dicMaladies))
data_GpM.df <- apply(data_GpM, 1, term.frequency)
data_GpM.idf <- apply(data_GpM, 2, inverse.doc.frequency)
data_Gpm.tfidf <-  apply(data_GpM.df, 2, tf.idf, idf = data_GpM.idf)

####reduction de la taille de la matrice pour les tests avant production #### 
rangMaladies=order(rowSums(data_Gpm.tfidf),decreasing=T)[c(1:50)];length(rangMaladies) #### ON prend les 500 premières maladies importantes dans le tf-idf
data_used=t(data_GpM[,rangMaladies]);dim(data_used) #### matrice 500x16591 non normalisée
data_used=data_used[,which(colSums(data_used) > 0)];dim(data_used);View(data_used)
data_GpM.df <- apply(data_used, 1, term.frequency)#### on refait un tfidf sur la matrice précédente pour récupérer les indices des gènes importants sur les maladies restantes
data_GpM.idf <- apply(data_used, 2, inverse.doc.frequency)
data_Gpm.tfidf <-  apply(data_GpM.df, 2, tf.idf, idf = data_GpM.idf);dim(data_Gpm.tfidf)
rangGenes=order(rowSums(data_Gpm.tfidf),decreasing=T)[c(1:100)];length(rangGenes) ### on prend les 6000 gènes les plus important
data_used=data_used[,rangGenes];dim(data_used)####on a une matrice 1500x6000 avec des trucs représentatifs
View(data_used)
 #### on garde les lignes utiles et pas là ou les maladies ne sont plus représentées du tout

#####tfidf de la matrice créée####
data_used.df <- apply(t(data_used), 1, term.frequency)
data_used.idf <- apply(t(data_used), 2, inverse.doc.frequency)
data_used.tfidf <-  apply(data_used.df, 2, tf.idf, idf = data_used.idf);dim(data_used.tfidf)
View(data_used.tfidf) #### ET ON A ENFIN UNE MATRICE PLAISANTE REDUITE pour les tests 500x1000 sans ligne/colonne à 0 avec des maladies représentatives


#####NMF ensemble de TESTS pre Prod#####
weight=Matrix(rep(1,dim(data_used.tfidf)[1]*dim(data_used.tfidf)[2]),nrow=dim(data_used.tfidf)[1]);dim(weight)###Création d'une matrice de poids pour l'appel de lsnmf
res=nmf(data_used.tfidf,6,method="ls-nmf", .options="vt",seed='random',weight=as.matrix(weight)) ###methode test Ls-nmf random sur petite matrice
res.coef <- coef(res)####on récupère H
res.bas <- basis(res)####on récupère W

####Pour chacun des clusters on affiche les top genes + wordcloud des topgenes
for (n in seq(1, 6, 1)) {
  freq <- res.coef[n,(order(res.coef[n,], decreasing = TRUE) [1:10])]
  wordcloud(names(freq), freq, scale = c(0.1, 3), colors = brewer.pal(6, "Dark2"))
  print(freq)
  print("==========================")
}
###Visualisation clusters
comparison.cloud(t(res.coef)) #H
comparison.cloud(res.bas) #W

####Barplots
res.bas[(order(res.bas[,1], decreasing = TRUE) [1:40]),1]
barplot(res.bas[(order(res.bas[,6], decreasing = TRUE) [1:40]),6])
barplot(res.coef[6,(order(res.coef[6,], decreasing = TRUE) [1:40])])

x=c("")
for (n in seq(1, 6, 1)) {
  print(res.coef[n,(order(res.coef[n,], decreasing = T) [1:3])])
}

res.bas[(order(res.bas[,1], decreasing = TRUE) [1:40]),1]




######Production#####
data_used.tfidf=t(data_Gpm.tfidf)
weight=Matrix(rep(1,dim(data_used.tfidf)[1]*dim(data_used.tfidf)[2]),nrow=dim(data_used.tfidf)[1]);dim(weight)
#####Methode d'elbow pour skmeans #####
k.max <- 25
wss <- sapply(2:k.max, 
              function(k){skmeans(data_used.tfidf, k,control = list(verbose = TRUE))$value})
wss
plot(2:k.max, wss,
     type="b", pch = 19, frame = FALSE, 
     xlab="Number of clusters K",
     ylab="Value of the criterion")
findElbow(wss) ####nombre de clusters pour la methode Skmeans sur le jeu de données.

sk=skmeans(data_used.tfidf,10,control = list(verbose = TRUE));dim(sk$prototypes) # Skmeans sur le meilleur k et affichage de la dimension des prototypes
init <- nmfModel(10, data_used.tfidf, W=1, H=sk$prototypes)###creation de la methode de seeding via les résultats du spherical kmeans
nmfSpherical=nmf(data_used.tfidf,10,method="ls-nmf",.options="vt",seed=init,weight=as.matrix(weight)) ####NmfSpherical

nmfRandomK=nmfEstimateRank(data_used.tfidf,c(5:15),method="ls-nmf",.options="vt",seed="random",weight=as.matrix(weight),nrun=3);plot(nmfRandomK) #calcul et affichage du meilleur rang K pour random
nmfRandom=nmf(data_used.tfidf,8,method="ls-nmf",.options="vt",seed="random",weight=as.matrix(weight)) #calcul pour rang 8 random

nmfIcaK=nmfEstimateRank(data_used.tfidf,c(5:15),method="ls-nmf",.options="vt",seed="ica",weight=as.matrix(weight),nrun=3);plot(nmfIcaK) #calcul et affichage du meilleur rang K pour Ica
nmfIca=nmf(data_used.tfidf,7,method="ls-nmf",.options="vt",seed="Ica",weight=as.matrix(weight)) #calcul pour rang 7 Ica

nmfNndsvdK=nmfEstimateRank(data_used.tfidf,c(5:15),method="ls-nmf",.options="vt",seed="nndsvd",weight=as.matrix(weight),nrun=3);plot(nmfNndsvdK) #calcul et affichage du meilleur rang K pour Nndsvd
nmfNndsvd=nmf(data_used.tfidf,7,method="ls-nmf",.options="vt",seed="nndsvd",weight=as.matrix(weight)) #calcul pour rang 7 nndsvd

###recuperation des features
snmf=extractFeatures(nmfSpherical,method="max")
rnmf=extractFeatures(nmfRandom,method="max")
inmf=extractFeatures(nmfIca,method="max")
nnmf=extractFeatures(nmfNndsvd,method="max")

listnmf=list(nmfSpherical,nmfRandom,nmfIca,nmfNndsvd) #creation liste des nmf réalisées
compare(listnmf) #comparaison des résultats
#affichage des résidus de chaque méthode et convergence.
plot(nmfSpherical)
plot(nmfRandom)
plot(nmfIca)
plot(nmfNndsvd)



####à réaliser pour chaque methode d'initialisation:
res.coef <- coef(nmfSpherical)####on récupère H
res.bas <- basis(nmfSpherical)####on récupère W

##recuperation des basismap + consensusmap des matrices à réaliser pour chaque nmf
png(filename = "test1.png", width = 450, height = 450,
    pointsize = 12, bg = "white",  res = NA)
par( mfrow = c( 1, 2 ) )
basismap(res)
coefmap(res)
dev.off()


#affichage du wordcloud des matrices
dev.new(width=25000, height=25000)
comparison.cloud(t(res.coef))
comparison.cloud(res.bas)

##recuperation top terms
res.bas[(order(res.bas[,1], decreasing = TRUE) [1:40]),1]
barplot(res.bas[(order(res.bas[,6], decreasing = TRUE) [1:40]),6])
barplot(res.coef[6,(order(res.coef[6,], decreasing = TRUE) [1:40])])


for (n in seq(1, 10, 1)) {
  freq <- res.coef[n,(order(res.coef[n,], decreasing = TRUE) [1:10])]
  wordcloud(names(freq), freq, scale = c(0.1, 3), colors = brewer.pal(6, "Dark2"))
  print(freq)
  print("==========================")
}

x=c("")
for (n in seq(1, 10, 1)) {
  print(res.coef[n,(order(res.coef[n,], decreasing = T) [1:3])])
}

res.bas[(order(res.bas[,1], decreasing = TRUE) [1:40]),1]


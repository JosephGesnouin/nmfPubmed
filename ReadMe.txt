
#################################################################################
################# MLDS 5 Factorisation matricielle non négative #################
#################################################################################

Authors: Joseph Gesnouin & Cristel Dos Santos Catarino



I. Folders list
------------
Données Fournies		Contient l'ensemble des documents fournis au début du pojet, un readme est disponible à l'interieur du dossier précisant le contenu de chaque fichier du dossier, ceci est 				également précisé dans le rapport rubrique "Dispositifs et outils de développement"

CreationBDD			Contient l'ensemble des scripts python et bash relatifs à la création et aux requêtes PUBMED via le package biopython, dispose de deux sous dossiers séparant la création 
				initiale de la base de données puis l'amélioration de celle ci en corrélant l'information des multiples fichiers disponibles initialement. Un readme est également 					disponible dans le sous dossier 1 afin de comprendre l'utilité de chaque fichier.

NMF				Contient la matrice générée précédemment et l'ensemble des fichiers R relatifs à l'utilisation des algorithmes de machine learning: NMF / Spherical kmeans sur le jeu de 				données un readme est également disponible.


II. Expected Programs
------------------------

Il est attendu de l'utilisateur d'avoir une version de Python ainsi que de R sur sa machine si il souhaite relancer les scripts. Certains scripts bash supervisant la mise en place d'un système de backup pour les requêtes  nécessitent également l'utilisation d'un système Unix. Les librairies sont chargées au début de chaque script il sera sans doute nécéssaire de les télécharger au préalable si besoin est.

###Librairies Python:
-scipy.sparse
-Bio
-numpy
-panda
-sklearn
-sys

###Libraries R:
-readr				
-Matrix				
-NMF				
-tidytext			
-tm				
-slam				
-dplyr				
-SnowballC
-skmeans			
-textir
-stm				
-factoextra
-foreach
-doParallel			
-fastICA
-wordcloud
-topicmodels



III. Questions
------------------------
Si vous avez des difficultés à faire tourner les programmes ne pas hésiter à nous envoyer un mail à jgesnouin@gmail.com ou bien cristel.catarino@gmail.com pour de plus amples informations
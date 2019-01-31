
#################################################################################
################# MLDS 5 Factorisation matricielle non négative #################
#################################################################################

Authors: Joseph Gesnouin & Cristel Dos Santos Catarino



Fichiers contenus dans le dossier:

##findElbow.R##
Fonction nous permettant de trouver le rang correct pour le spherical Kmeans

##tfidf.R##
Contient notre implémentation de l'algorithme tfidf

##brute.csv##
Matrice générée sur laquelle nous travaillons

##ScriptFinal.R##

Le script est décomposé en deux parties: 
	-une partie dite de test sur une matrice de taille minime: 50*100 afin de s'assurer du bon fonctionnement de tous les packages, et également utile dans le cas ou l'on nous demande une présentation lors de l'oral
	-une partie dite de production ou la matrice est de taille 4000*16000, il est nécéssaire d'avoir une puissance de calcul suffisante ou des serveurs cloud pour faire tourner ces fonctions.
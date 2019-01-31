
#################################################################################
################# MLDS 5 Factorisation matricielle non négative #################
#################################################################################

Authors: Joseph Gesnouin & Cristel Dos Santos Catarino



Nous allons principalement présenter les fichiers contenus dans CreationBDD1_Human_disease, le deuxième dossier étant foncièrement équivalent au premier avec des jeux de données différents.

Fichiers contenus dans le dossier 1:

##automatique.py##	
script python permettant de faire des requêtes Pubmed: en fonction d'un couple gene/maladie, permet de récuperer le nombre d'articles pubmed référencés traitant de cette association.


##size.py##
script python permettant d'avoir des informations relatives au fichier créé: nombre de maladies, nombre de genes, nombre de couples genes/maladies stockés, nombre moyen de gênes caractérisant une maladie, nombre moyen de genes en commun entre deux maladies.

##outputTestAuto.txt##
Fichier texte contenant le résultat du script automatique.py

##human_disease_textmining_full.tsv##
fichier de base que nous utilisons pour les requetes

##ThankMisterOsman.sh##
Nous lançons automatique.py via ce script, le nombre de requetes pubmed par seconde étant limitées et les serveurs n'étant pas fiable, ce shell nous permet de relancer de manière automatique les requetes pubmed là ou l'on s'est arrété de manière automatique si les serveurs arrêtent de répondre, les requetes prenant environ 4-5 jours cela nous a permis de ne pas avoir le nez collé à notre machine pendant les requetes. Relance le script toutes les 80s

##verif.sh## 
permet de verrifier que la ligne x du fichier sortie correspond bien au couple gene maladie de la ligne x du fichier entrée, cela nous permet de nous assurer que l'automatisation de nos requetes est correcte

##Dossier Backup##
Nous avons sauvegardé nos requetes de manière régulière afin de ne pas avoir à les refaire  dans le cas ou les serveurs pubmed ne répondaient plus ce qui n'est pas si rare.


##toCsv.py## 
transforme le fichier text sortie en fichier Csv que nous utilisons dans la suite (dossier NMF)
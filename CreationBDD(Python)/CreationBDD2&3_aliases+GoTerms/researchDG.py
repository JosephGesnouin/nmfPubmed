#!C:/Users/Cristel Catarino/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6
#!/usr/lib/python3.5


from Bio import Entrez, SeqIO, Medline
import scipy.sparse as sp
import numpy as np
import pandas as pd
import sklearn
import sys

Entrez.email = "kikagomes23@gmail.com"

def recupDictionnaires():
    ens = []
    file = open("dict.txt", "r")
    doc = file.read()
    dim = len(doc.split("##"))
    i = 0
    print ("STARTING RECUP")
    for line in doc.split("##"):

        if (i < dim-1):
            symbol, aliases, name, diseases, goTerms, pubmedIds = line.split("|")
            dico = {}
            dico['symbol'] = symbol
            dico['aliases'] = []
            for alias in aliases.split(","):
                if (not alias == ""):
                    dico['aliases'].append(alias)
            dico['name'] = name
            dico['diseases'] = []
            for disease in diseases.split(","):
                if (not disease == ""):
                    dico['diseases'].append(disease)
            dico['goTerms'] = []
            for goTerm in goTerms.split(","):
                if (not goTerm == ""):
                    dico['goTerms'].append(goTerm)
            dico['pubmedIds'] = []
            for pubmedId in pubmedIds.split(","):
                if (not pubmedId == ""):
                    dico['pubmedIds'].append(pubmedId)
            ens.append(dico)
            #print (dico)
        i += 1
    print ("END RECUP")
    return ens

def pbmd_search(maladie,gene):

    handle = Entrez.esearch(db = 'pubmed', term = maladie + " AND " + gene, retmax = '1000000000')
    print (maladie + " AND " + gene)
    result = Entrez.read(handle)
    handle.close()
    return(result)

def ecriture_file(maladie, gene, value):

    output = open('output.txt', 'a')
    output.write(maladie+"|" +gene+ "|" + str(value) + "##")
    output.close()

def ecriture_end_dg():
    output = open('output.txt', 'a')
    output.write("@@")
    output.close()

if __name__ == '__main__':

    print("################### START SEARCHING ###################")

    ###### RECUPERATION DE LA LISTE DES DICTIONNAIRES DE GENES
    ens = recupDictionnaires()
    dim = len(ens)
    print (dim)

    ###### OUVERTURE DU FIHCIER D'OUTPUT ET VERIFICATION DE SON CONTENU POUR REPRISE DE LA RECHERCHE
    try :
        file = open("output.txt", "r")
    except IOError:
        file = open("output.txt", "x")
        file = open("output.txt", "r")

    doc = file.read()

    file.close()

    lim = 0
    already = doc.split("@@")
    for line in already:
        lim += 1
    finalPart = already[-1]
    print (finalPart)
    print (lim)

    delim = 0
    for part in finalPart.split("##"):
        delim += 1

    i = 0
    #while (i < dim):

    ###### POUR CHAQUE DICTIONNAIRE :
    for dico in ens:

        print ("Loading...")
        print(str(i+1) + "/" + str(dim))

        # S'IL EST DEJA ECRIT DANS LE FICHIER, PASSER AU SUIVANT
        if (i < lim -1):
            print ("... GENE : Already done")

        # SINON :
        # VERIFIER QUELLES MALADIES ONT DEJA ETE ECRITES
        else :

            print ("Preparing GENE...")

            # PREPARATION DE LA REQUETE
            genes = set([])
            if (not len(dico['aliases']) == 0):
                genes.update(dico['aliases'])
            if (not len(dico['symbol']) == 0):
                genes.add(dico['symbol'])
            if (not len(dico['name']) == 0):
                genes.add(dico['name'])

            genes_string = " OR ".join(genes)
            genes_string = "(" + genes_string + ")"

            print ("GENE : ", genes_string)

            nbD = len(dico['diseases'])
            cptD = 0

            #while (cptD < nbD):

            ##### POUR CHAQUE MALADIE
            for disease in dico['diseases']:

                # SI DEJA FAIT
                if (cptD < delim -1):
                    print(str(cptD+1) + "/" + str(nbD))
                    print ("... DISEASE Already done")

                # SI PAS ENCORE FAIT
                else:

                    # REQUETE PUBMED
                    print ("SEARCHING DISEASE (" + str(cptD+1) + "/" + str(nbD) + ")" )
                    result = []
                    idList = set([])
                    result = pbmd_search(disease,genes_string)
                    idList.update(result['IdList'])

                    key = len(idList)
                    key = key + 1
                    print("PRINTING IN FILE ...")
                    ecriture_file(disease, dico['symbol'], key)
                    print ("***** OK !!")

                cptD += 1

            ecriture_end_dg()
            delim = 0

        i+=1

    print("################### END SEARCHING ###################")

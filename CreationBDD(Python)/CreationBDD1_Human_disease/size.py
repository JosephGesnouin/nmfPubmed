import scipy.sparse as sp
from Bio import Entrez, SeqIO, Medline
import numpy as np
import pandas as pd
import sklearn


Entrez.email = "jzkftw@gmail.com"

data = {}
maladies = set([])
genestab = set([])


####Manip fichier open
file=open("outputTestAuto.txt","r",encoding='utf-8')
i=0
for line in file:
        i=i+1
        maladie,genes,numero=line.split("| ")
        maladies.update([maladie])
        genestab.update([genes])
print("on a ",len(maladies)," maladies uniques")
print("on a ",len(genestab)," genes uniques")
print("on a ",i, "couples genes maladies traités")
print("il y'a environ", len(maladies)*len(genestab), "couples existants il faudrait environ ", len(maladies)*len(genestab)/3/3600/24, "jours pour réaliser toutes les queries")
print("il faut en moyenne ", i/len(maladies), "genes pour déterminer une maladie soit environ ", i/len(maladies)/len(genestab)*100, " % du génome requis pour définir une maladie")


"""for maladie in maladies:
        print(maladie)"""
        
        

"""
####Manip fichier close
output = open('output.txt', 'w')

for maladie in maladies:
    for gene in genestab:
        key = (maladie, gene)
        if key in data:
            output.write(maladie+"| " +gene+ "| " + data[(maladie,gene)])
            output.write("\n")
output.close()"""

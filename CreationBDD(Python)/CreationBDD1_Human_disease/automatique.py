import scipy.sparse as sp
from Bio import Entrez, SeqIO, Medline
import numpy as np
import pandas as pd
import sklearn
import sys

lim=int(sys.argv[1])

Entrez.email = "jzkftw@gmail.com"

data = {}
maladies = set([])
genestab = set([])


#### Manip query
def pbmd_search(maladie,gene):
    handle = Entrez.esearch(db='pubmed',term=maladie+" "+gene)
    result=Entrez.read(handle)
    print(result['Count'])
    return(result['Count'])
    
def ecriture_file(maladie,gene):
     output = open('outputTestAuto.txt', 'a')
     key = pbmd_search(maladie,gene)
     key=int(key)+1
     output.write(maladie+"| " +gene+ "| " + str(key))
     output.write("\n")
     output.close()


####Manip fichier open
file=open("human_disease_textmining_full.tsv","r")
i=0
for line in file:
        if(i < lim):
            i+=1
            print(i)
        else:
            idi,gene,numero,maladie,temp1,temp2=line.split("\t")
            print(gene)
        #data[(maladie,gene)]=pbmd_search(maladie,gene)
        #genestab.update([gene])
            ecriture_file(maladie,gene)
            print("nouvelle maladie numero ", i, "sur 641 618")
            print(maladie)
            i=i+1
        #maladies.update([maladie])

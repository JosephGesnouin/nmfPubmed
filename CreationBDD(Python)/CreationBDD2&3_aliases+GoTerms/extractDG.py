#!/usr/bin/python

# Extraction des genes dans la base de données Entrez-Gene et Gene Ontology
def extractGenes1():
    print ("**********ETAPE 1 \n")
    ens = []
    file = open("EntrezGene.txt","r")
    for line in file:
        idGene, symbGene, aliasGene, resumeGene, numK, emplacement = line.split("\t")
        dico = {}
        dico['symbol'] = symbGene
        dico['aliases'] = []
        dico['name'] = ""
        dico['goTerms'] = []
        dico['pubmed'] = []
        for alias in aliasGene.split(","):
            dico['aliases'].append(alias)
        ens.append(dico)
    file.close()
    print ("**********ETAPE 1 ******** END \n")
    return ens

def extractGenes2():
    print ("**********ETAPE 2 \n")
    ens = extractGenes1()

    for dico in ens:
        file = open("gene_association.goa_ref_human","r")
        for line in file:
            tmp1,tmp2,nomGene,tmp3,idGO,idPUBMED,tmp4,tmp5,tmp6,nameGene,aliasGene,tmp7,tmp8,tmp9,tmp10,tmp11,tmp12 = line.split("\t")
            if (nomGene == dico['symbol']) or (nomGene in dico['aliases']):
                dico['name'] = nameGene
                if (not idGO in dico['goTerms']):
                    dico['goTerms'].append(idGO)
                if (not idPUBMED in dico['pubmed']):
                    dico['pubmed'].append(idPUBMED)
                for alias in aliasGene.split("|"):
                    if(not alias in dico['aliases']):
                        dico['aliases'].append(alias)
        file.close()
        print ("**********ETAPE 2 ******** END \n")
        return ens

def extractGenes3():

    print ("**********ETAPE 3 \n")

    ens = extractGenes2()
    for dico in ens:
        file = open("Homo sapiens-20140521.tsv","r")
        for line in file:
            tmp1, tmp2, nameA, nameB, tmp3, tmp4, method, tmp5, idPUBMED, tmp6, tmp7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, roleA, roleB, tmp14 = line.split("\t")
            if (len(nameA.split(":")) == 2):
                part1, part2 = nameA.split(":")
                if (len(part2.split(":")) == 2):
                    geneA, tmp = part2.split("(")
                    if (geneA == dico['symbol']) or (geneA in dico['aliases']):
                        if (not idPUBMED in dico ['pubmed']):
                            dico['pubmed'].append(idPUBMED)
            if (len(nameB.split(":")) == 2):
                part1, part2 = nameB.split(":")
                if (len(part2.split(":")) == 2):
                    geneB, tmp = part2.split("(")
                    if (geneB == dico['symbol']) or (geneB in dico['aliases']):
                        if (not idPUBMED in dico ['pubmed']):
                            dico['pubmed'].append(idPUBMED)
        file.close()
        print ("**********ETAPE 3 ******** END \n")
        return ens

def extractGenes4():
    print ("**********ETAPE 4 \n")
    ens = extractGenes3()

    lim = 0

    try :
        file = open("dict.txt", "r")
    except IOError:
        file = open("dict.txt", "x")
        file = open("dict.txt", "r")

    doc = file.read()
    for line in doc.split(" # "):
        lim += 1

    print (lim)

    dim = len(ens)
    print (dim)

    i = 0

    while (i < dim):

        for dico in ens:

            if (i < lim -1):
                print ("... Already done")
                print(str(i+1) + "/" + str(dim))


            else :
                print ("Loading...")
                print(str(i+1) + "/" + str(dim))
                dico['disease'] = []
                file = open("human_disease_textmining_full.tsv","r")
                for line in file:
                    identifiant,symbGene,idMaladie,nomMaladie,tmp1,tmp2 = line.split("\t")
                    if (symbGene == dico['symbol']) or (symbGene in dico['aliases']):
                        if(not nomMaladie in dico['disease']):
                            dico['disease'].append(nomMaladie)
                file.close()
                ecrireDico(dico)
                print ("***** OK !!")

            i+=1

    print ("**********ETAPE 4 ******** END \n")
    return ens


def ecrireDico (dico):
    output = open('dict.txt', 'a')
    output.write(dico['symbol'] + "|" + ",".join(dico['aliases']) + "|" + dico['name'] + "|" + ",".join(dico['disease']) + "|" + ",".join(dico['goTerms']) + "|" + ",".join(dico['pubmed']) + "##")
    output.close()

if __name__ == '__main__':

    print("################### EXTRACTION START ###################")
    genesData = extractGenes4()
    print("################### EXTRACTION END ###################")

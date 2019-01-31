#!/usr/bin/python

# Extraction des genes dans la base de données Entrez-Gene et Gene Ontology
def nettoyerChaine():
    file = open('output2.txt', 'r')
    output = file.read()
    file.close()
    output = output.replace("@",'')
    return output


def ecrireChaine(chaine):
    file = open('cleaned.txt', 'x')
    file = open('cleaned.txt', 'w')
    for line in chaine.split("##"):
        file.write(line)
        file.write("\n")
    file.close()

if __name__ == '__main__':

    print("################### CLEANING START ###################")

    print("***** CLEAN")
    data = nettoyerChaine()
    print("***** WRITE")
    ecrireChaine(data)
    print("***** END")

    print("################### CLEANING END ###################")

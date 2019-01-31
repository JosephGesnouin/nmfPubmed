===========================================================================================================================================================
																OMIM database 
===========================================================================================================================================================


OMIM est une base de données décrivant des associations gènes/maladies. 

morbidmap.txt : Contient 6664 records, chaque record contient 4 champs séparés par des "|"

exemple d'extrait de la base : Asthma and nasal polyps, 208550 (3)|TBX21, TBET|604895|17q21.32

description des champs:
1  - Maladie, <maladie MIM no.> (<Numero - voir ci dessous la signification>)
2  - Gene conserné ainsi que ses alias
3  - Numero OMIM
4  - Emplacement cytogénétique


Signification du numéro entre parenthèses qui apparrait après le nom de la maladie

1 - la maladie est placée sur la carte en fonction de son association avec le gène, mais l'anomalie génétique sous-jacente n'est pas connue.
2 - la maladie  a été placé sur la carte par une liaison; aucune mutation n'a été trouvé.
3 - la base moléculaire de la maladie est connu; une mutation a été trouvé dans le gène.
4 -  syndrome de gènes contigus, plusieurs gènes sont supprimés ou dupliqués provoquant le phénotype.

===========================================================================================================================================================
														DISEASES database
============================================================================================================================================================

Fichier : human_disease_textmining_full.tsv

Ressemble a OMIM puisque cette base contient des associations gènes/maladies. Cependant, cette base contient plus d'informations que OMIM car elle contient 
les association connues (telle que OMIM) mais aussi les associations issues d'etudes de text mining ainsi que d'etudes de GWAS (genome-wide associations studies)
 
Nombre de records : 641618
separateurs : tabulations

exemple d'extrait de la base :   ENSP00000001008	FKBP4	DOID:2841	Asthma	1.490	0.7

ENSP00000001008 : identifiant unique de l'association
FKBP4 : symbole officiel du gène considéré
DOID:2841 : identifiant unique de la maladie (provient de disease ontology)
Asthma : nom de la maladies

Ne pas considerer les deux derniers champs

===========================================================================================================================================================
																	Gene Ontology database :
===========================================================================================================================================================

contient une description des produits des gènes (proteines) (et donc une définition de leur fonctions).
chaque  fonction de gène est définie par un GO term, chaque GO term a un identifiant. 


Deux fichiers textes :

Le fichier gene_association_goa_ref_human : 354285 records, chaque record contient 
UniProtKB	Q96QA5	GSDMA		GO:0006915	PMID:17471240	IDA		P	Gasdermin-A	GSDMA_HUMAN|GSDMA|GSDM|GSDM1|FKSG9	protein	taxon:9606	20080708	UniProt		

Les champs importants sont : 
GSDMA : nom du gene
GO:0006915 : GO terme ID ( identifiant du Gene Ontology term) 
PMID:17471240 : PUBMED identifiant de l'article presentant la fonction du gène 
Gasdermin-A	GSDMA_HUMAN|GSDMA|GSDM|GSDM1|FKSG9 : Alias des gènes 


Le fichier Go_terms : 37104 records, chaque record contient 3 champs

exemple d'extrait de la base : 

GO:2001286		regulation of caveolin-mediated endocytosis	P	

1 : identifiant du GO term
2 : Le GO term 
3 : Il y a trois lettres possibles :
	P : signifie bilogical process 
	F : molecular function
	C : cellular component
	
	
===========================================================================================================================================================
																		Entrez-gene Database 
===========================================================================================================================================================
Fichier EntrezGene

Nombre de records : 19063
separateur : tabulation

exemple d'extrait de la base:

340273	ABCB5	ABCB5alpha, ABCB5beta, EST422562	ABCB5 belongs to the ATP-binding cassette (ABC) transporter superfamily of integral membrane proteins...	7	7p21.1

1 - identifiant du gène : 340273
2 - Symbole officiel : ABCB5
3 - Aliases du gène : ABCB5alpha, ABCB5beta, EST422562
4 - Summary du gène (petit résumé de la fonction du gène) : ABCB5 belongs to the ATP-binding
5 - Numero du chromosome : 7	
6 - Emplacement cytogénétique : 7p21.1


============================================================================================================================================================
															Pina database	
============================================================================================================================================================

fichier HOMO sapiens-20140521.tsv

Description des interactions entre gènes 

166776 records 

exemple d'extrait de la base :

uniprotkb:P0CG48	uniprotkb:Q96QA5	uniprotkb:UBC(gene name)	uniprotkb:GSDMA(gene name)	-	-	MI:0004(affinity chromatography technology)	-	pubmed:21139048	taxid:9606(Homo sapiens)	taxid:9606(Homo sapiens)	MI:0915(physical association)	(biogrid)	BIOGRID_167698	-	bait	prey	go:GO:0006977|go:GO:0006281|go:GO:0000080|go:GO:0000082|go:GO:0007249|go:GO:0007254|go:GO:0000216|go:GO:0002755|go:GO:0007220|go:GO:0007219|go:GO:0000084|go:GO:0050852|go:GO:0035666|go:GO:0008063|go:GO:0000187|go:GO:0031145|go:GO:0006916|go:GO:0002479|go:GO:0006915|go:GO:0016044|go:GO:0019221|go:GO:0005829|go:GO:0046788|go:GO:0030666|go:GO:0016197|go:GO:0010008|go:GO:0007173|go:GO:0008543|go:GO:0008624|go:GO:0045087|go:GO:0016071|go:GO:0042059|go:GO:0000122|go:GO:0030512|go:GO:0032480|go:GO:0051436|go:GO:0048011|go:GO:0005654|go:GO:0070423|go:GO:0005886|go:GO:0043123|go:GO:0051092|go:GO:0045944|go:GO:0051437|go:GO:0000209|go:GO:0061418|go:GO:0034130|go:GO:0034134|go:GO:0034138|go:GO:0034142|go:GO:0006367|go:GO:0007179	go:GO:0006915|go:GO:0006917|go:GO:0048471	unspecified:32644

le "-" indique q'il n y a pas d'information pour ce champ
separateur : tabulation 

champs importants :

-uniprotkb:UBC(gene name) :  nom de l'interacteur A (UBC)

-uniprotkb:GSDMA(gene name) : nom de l'interacteur A (GSDMA) 

-MI:0004(affinity chromatography technology) : methode de detection  d'interaction 

-pubmed:21139048 : PUBMED identifiant de la publication 

-go:GO:0006977|go:GO:0006281|go:GO:0000080| .... : Role experimental de l'interacteur A (GO term identifiants)

-go:GO:0006915|go:GO:0006917|go:GO:0048471 : Role experimental de l'interacteur B (GO term identifiants)


																

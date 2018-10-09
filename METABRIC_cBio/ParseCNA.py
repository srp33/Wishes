import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

#Function used to interpret data_CNA.txt values
def geneAlterationTranslator(int):
	if int== '-2':
		return "Homozygous deletion"
	if int=='-1':
		return "Heterozygous deletion"
	if int =='1':
		return "Low-level amplification"
	if int=='2':
		return "High-level amplification"
	return "Normal";

cnaFile = open(inFilePath,"r")
cnaHeaders = cnaFile.readline().rstrip("\n").split("\t")
del cnaHeaders[1]

cnaDict = {}
for sample in range(1, len(cnaHeaders)):
    cnaDict[cnaHeaders[sample]]  = {}

genes = []
for line in cnaFile:
    line = line.rstrip("\n").split("\t")
    del line[1]
    gene = line[0]

    genes.append(gene)

    for sampleIndex in range(1, len(line)):
        cnaDict[cnaHeaders[sampleIndex]][gene] = geneAlterationTranslator(line[sampleIndex])

cnaFile.close()

genes = sorted(list(genes))

with open(outFilePath, "w") as outFile:
    outFile.write(("\t".join(["Sample"] + genes) + "\n"))

    for sample in cnaDict:
        sampleList = [sample] + [cnaDict[sample][gene] for gene in genes]
        outFile.write(("\t".join(sampleList) + "\n"))

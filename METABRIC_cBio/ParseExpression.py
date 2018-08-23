import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

dataFile = open(inFilePath,"r")
dataHeaders = dataFile.readline().rstrip("\n").split("\t")
del dataHeaders[1]

dataDict = {}
for sample in range(1, len(dataHeaders)):
    dataDict[dataHeaders[sample]]  = {}

genes = []
for line in dataFile:
    line = line.rstrip("\n").split("\t")
    del line[1]
    gene = line[0]

    genes.append(gene)

    for sampleIndex in range(1, len(line)):
        dataDict[dataHeaders[sampleIndex]][gene] = line[sampleIndex]

dataFile.close()

genes = sorted(list(genes))

with gzip.open(outFilePath, "w") as outFile:
    outFile.write(("\t".join(["Sample"] + genes) + "\n").encode())

    for sample in dataDict:
        sampleList = [sample] + [dataDict[sample][gene] for gene in genes]
        outFile.write(("\t".join(sampleList) + "\n").encode())

import sys, gzip

inFilePath = sys.argv[1]

dataDict = {}
genes = set()
vcs = set()

with open(inFilePath) as inFile:
    inFile.readline() # Remove comment line
    headerItems = inFile.readline().rstrip("\n").split("\t")
    geneIndex = headerItems.index("Hugo_Symbol")
    sampleIndex = headerItems.index("Tumor_Sample_Barcode")
    vcIndex = headerItems.index("Variant_Classification")

    for line in inFile:
        line = line.rstrip("\n").split("\t")
        gene = line[geneIndex]
        sample = line[sampleIndex]
        vc = line[vcIndex].replace("'", "_prime_")

        if sample not in dataDict:
            dataDict[sample] = {}

        dataDict[sample][gene] = dataDict[sample].setdefault(gene, []) + [vc]
        genes.add(gene)
        vcs.add(vc)

genes = sorted(list(genes))
vcs = sorted(list(vcs))

def getSampleValue(dataDict, sample, gene, vc):
    if gene in dataDict[sample]:
        if vc in dataDict[sample][gene]:
            return "Yes"

    return "No"

for vc in vcs:
    outFilePath = "Variant_{}.tsv".format(vc)

    vcDict = {}
    vcGenes = set()
    for sample in dataDict:
        for gene in dataDict[sample]:
            if vc in dataDict[sample][gene]:
                vcGenes.add(gene)

    vcGenes = sorted(list(vcGenes))

    with open(outFilePath, "w") as outFile:
        outFile.write(("\t".join(["Sample"] + vcGenes) + "\n"))

        for sample in dataDict:
            sampleList = [sample] + [getSampleValue(dataDict, sample, gene, vc) for gene in vcGenes]
            outFile.write(("\t".join(sampleList) + "\n"))

import sys, gzip

inFilePath = sys.argv[1] #"expression_main.txt"
outFilePath = sys.argv[2] #"metaData.txt"

uniqueSampleIDs = []
sampleAttributes = {}

#Read in metaData and fill sampleAttributes Dictionary
with open(inFilePath, 'r') as inFile:
    inHeaderItems = inFile.readline().rstrip("\n").split("\t")

    sampleName = inHeaderItems.index("IDENTIFIER")
    sampleGender = inHeaderItems.index("sex")
    sampleGenotype = inHeaderItems.index("genotype")
    sampleColor = inHeaderItems.index("color")

    for line in inFile:
         lineItems = line.rstrip("\n").split("\t")
         mouse = lineItems[sampleName]
         gender = lineItems[sampleGender]
         genotype = lineItems[sampleGenotype]
         color = lineItems[sampleColor]

         if genotype == "WT":
             genotype = "Wild Type"
         elif genotype == "K0":
             genotype = "Hras1-/-"
         if color == "A":
             color = "agouti (tan)"
         elif color == "W":
             color = "white (albino)"

         uniqueSampleIDs.append(mouse)
         sampleAttributes[mouse] = [gender,genotype,color]

uniqueSampleIDs = sorted(list(uniqueSampleIDs))


# Create output file
with gzip.open(outFilePath, 'w') as outFile:
    outText = "\t".join(["Sample","Variable","Value"]) + "\n"
    outFile.write(outText.encode())

    for sampleID in uniqueSampleIDs:
        dataItems = [] #To be filled with gene Values
        for sample in uniqueSampleIDs:
             metaData = sampleAttributes[sample]
             gender = metaData[0]
             genotype = metaData[1]
             color = metaData[2]

             outText = "\t".join([sample,"Sex",gender]) + "\n"
             outFile.write(outText.encode())

             outText = "\t".join([sample,"Germline Hras1 status",genotype]) + "\n"
             outFile.write(outText.encode())

             outText = "\t".join([sample,"Color",color]) + "\n"
             outFile.write(outText.encode())

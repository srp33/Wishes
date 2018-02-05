import sys, gzip

inFilePath = sys.argv[1] #"expression_main.txt"    
crypticPath = sys.argv[2] #"probe_attributes.txt"  #The gene types are cryptic, this file identifies them
outFilePath = sys.argv[3] #"data.txt" 

uniqueSampleIDs = []
uniqueGeneIDs = []

probeAttributes = {} #Dictionary to link identifier to actual gene
miceSamples = {} #Dictionary to link mice to Gene Values

#Build reference to decrypt genes
with open(crypticPath, 'r') as crypticFile:
    crypHeaderItems = crypticFile.readline().rstrip("\n").split("\t")

    geneIden = crypHeaderItems.index("IDENTIFIER")
    symbolIdentifier = crypHeaderItems.index("symbol")
    booleanIdentifier = crypHeaderItems.index("is_refseq") #I won't include data that is false in this column

    for line in crypticFile:
        lineItems = line.rstrip("\n").split("\t")
        identifier = lineItems[geneIden]
        geneSymbol = lineItems[symbolIdentifier]
        isRefSeq = lineItems[booleanIdentifier]
        if isRefSeq == "true":
            isRefSeq = True
        if isRefSeq == "false":
            isRefSeq = False	
        #Linking cryptic identifier to gene, and boolean for later reference
        #Gene is index #0, isRefSeq is index #1
        probeAttributes[identifier] = [geneSymbol,isRefSeq]


#Get a collection of each unique sample and gene in the dataset
with open(inFilePath, 'r') as inFile:
    inHeaderItems = inFile.readline().rstrip("\n").split("\t")

    geneIndex = inHeaderItems.index("IDENTIFIER")

    for mouse in inHeaderItems:
        if mouse != "IDENTIFIER":
            miceSamples[mouse] = {}
            uniqueSampleIDs.append(mouse)

    for line in inFile:
        inHeaderItems = line.rstrip("\n").split("\t")
        geneIdentifier = inHeaderItems[geneIndex]
        if geneIdentifier != "IDENTIFIER" and probeAttributes[geneIdentifier][1]:
            gene = probeAttributes[geneIdentifier][0]
            if gene not in uniqueGeneIDs:
                uniqueGeneIDs.append(gene)
            sampleSet = line.rstrip("\n").split("\t")
            sampleCount = -1 #To account for row name
            for sample in sampleSet:
                if sample != geneIdentifier:
                    sample = float(sample)
                    geneCount = 1.0
                    currentSample = uniqueSampleIDs[sampleCount]
                    if gene in miceSamples[currentSample]:
                        sample += miceSamples[currentSample][gene][0] #adds gene values to get average later
                        geneCount += miceSamples[currentSample][gene][1] #adds to count to calculate average later
                    miceSamples[currentSample][gene] = [sample,geneCount]
                sampleCount += 1


uniqueSampleIDs = sorted(list(uniqueSampleIDs))
uniqueGeneIDs = sorted(list(uniqueGeneIDs))

# Create output file
with gzip.open(outFilePath, 'w') as outFile:
    outText = "\t".join(["Sample"] + uniqueGeneIDs) + "\n"
    outFile.write(outText.encode())

    for sampleID in uniqueSampleIDs:
        dataItems = [] #To be filled with gene Values
        for geneID in uniqueGeneIDs:
             geneValue = miceSamples[sampleID][geneID][0]
             geneCount = miceSamples[sampleID][geneID][1]
             geneValue = "{0:.4f}".format(geneValue/geneCount)
             dataItems.append(geneValue)
        outText = "\t".join([sampleID] + dataItems) + "\n"
        outFile.write(outText.encode())

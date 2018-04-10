import sys, gzip

inFilePath = sys.argv[1] #"expression_main.txt"
outFilePath = sys.argv[2] #"data.txt"

tumorSamples = {} #To link tumor sample to a set of it's Hugo Values

uniqueSamples = [] #Keep track of what Tumor Samples there are

#Begin Parsing MetaData file
with open(inFilePath, 'r') as inFile:
        inHeaderItems = inFile.readline().rstrip("\n").split("\t")

        hugoIndex = inHeaderItems.index("Hugo_Symbol")
        tumorSampleIndex = inHeaderItems.index("Tumor_Sample_Barcode")
        deleteriousIndex = inHeaderItems.index("isDeleterious")

        for line in inFile:
                lineData = line.rstrip("\n").split("\t")
                isDeleterious = lineData[deleteriousIndex]
                if isDeleterious == "TRUE":
                        hugoValue = lineData[hugoIndex]
                        tumorSample = lineData[tumorSampleIndex]
                        if tumorSample not in tumorSamples:
                                tumorSamples[tumorSample] = []
                                uniqueSamples.append(tumorSample)
                        #Avoid duplicate Hugo Values for same tumor Sample
                        if hugoValue not in tumorSamples[tumorSample]:
                                tumorSamples[tumorSample].append(hugoValue)

uniqueSamples = sorted(list(uniqueSamples))

# Create output file
with gzip.open(outFilePath, 'a') as outFile:
        for sample in uniqueSamples:
                sampleHugoValues = tumorSamples[sample]
                for value in sampleHugoValues:
                        outText = "\t".join([sample,"SomaticMutation",value]) + "\n"
                        outFile.write(outText.encode())

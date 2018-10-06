import sys, gzip

inFilePath = sys.argv[1]
abbrevFilePath = sys.argv[2]
outFilePath = sys.argv[3]

abbrevDict = {}
with open(abbrevFilePath) as abbrevFile:
    for line in abbrevFile:
        lineList = line.strip('\n').split('\t')
        longerName = lineList[0]
        abbrev = lineList[1]
        abbrevDict[abbrev] = longerName

with gzip.open(inFilePath, 'r') as inFile:
    with open(outFilePath, 'w') as outFile:
        outFile.write(("\t".join(["Sample","Variable","Value"]) + "\n"))

        for line in inFile:
            lineList = line.decode().strip('\n').split('\t')
            #sampleID = lineList[0][:15]
            sampleID = lineList[0]
            cancerTypeAbbrev = lineList[1]
            cancerType = abbrevDict[cancerTypeAbbrev]

            outFile.write(("\t".join([sampleID, "Cancer Type", cancerType]) + "\n"))

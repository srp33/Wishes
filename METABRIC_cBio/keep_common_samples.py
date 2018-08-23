import gzip, sys

filePaths = sys.argv[1:]

commonSamples = None

for filePath in filePaths:
    with gzip.open(filePath) as dataFile:
        dataFile.readline()

        fileSamples = set()
        for line in dataFile:
            lineItems = line.decode().rstrip("\n").split("\t")
            fileSamples.add(lineItems[0])

        if commonSamples == None:
            commonSamples = fileSamples
        else:
            commonSamples = commonSamples & fileSamples

commonSamples = sorted(list(commonSamples))

for filePath in filePaths:
    outLines = []
    with gzip.open(filePath) as dataFile:
        outLines.append(dataFile.readline())

        dataDict = {}
        for line in dataFile:
            lineItems = line.decode().rstrip("\n").split("\t")
            dataDict[lineItems[0]] = lineItems

        for sample in commonSamples:
            outLines.append(("\t".join(dataDict[sample]) + "\n").encode())

    with gzip.open(filePath, "w") as dataFile:
        for line in outLines:
            dataFile.write(line)

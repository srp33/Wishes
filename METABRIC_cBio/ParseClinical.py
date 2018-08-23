import sys, gzip

inFilePath = sys.argv[1]
ignoreColumns = sys.argv[2].split(",")
outFilePath = sys.argv[3]

#There are 5 header lines. We want to focus on the first one.
with open(inFilePath, "r") as inFile:
    with gzip.open(outFilePath, "w") as outFile:
        headerItems = inFile.readline().rstrip("\n").split("\t")

        ignoreIndices = []
        for ignoreColumn in ignoreColumns:
            if ignoreColumn == "":
                continue
            if ignoreColumn in headerItems:
                ignoreIndices.append(headerItems.index(ignoreColumn))
            else:
                print("Cannot ignore {} column because it does not exist.".format(ignoreColumn))

        headerItems = [x for x in headerItems if x not in ignoreColumns]
        headerItems[0] = "Sample"

        inFile.readline()
        inFile.readline()
        inFile.readline()
        inFile.readline()

        outFile.write(("\t".join(headerItems) + "\n").encode())

        for line in inFile:
            lineItems = line.rstrip("\n").split("\t")

            lineItems = [lineItems[i] for i in range(len(lineItems)) if i not in ignoreIndices]

            for i in range(1, len(lineItems)):
                if lineItems[i] == "":
                    lineItems[i] = "NA"

            outLine = "\t".join(lineItems) + "\n"
            outFile.write(outLine.encode())

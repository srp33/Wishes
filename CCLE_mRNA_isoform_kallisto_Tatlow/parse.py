import re
import sys

expressionData = sys.argv[1]
outFile = sys.argv[2]

#write outFile, clinical on left expression on Right
with open(expressionData, 'r')  as inFile:
    with open(outFile, 'w') as outFile:
        outFile.write(inFile.readline())
        for line in inFile:
            lineList = line.strip('\n').split('\t')
            if re.search(r"\|", lineList[0]):
                index = re.search(r"\|", lineList[0]).start()
                lineList[0] = lineList[0][:index]
            outFile.write("\t".join(lineList) + "\n")

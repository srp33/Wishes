import re
import sys

expressionData = sys.argv[1]
clinicalAnnotations = sys.argv[2]
dataOutFile = sys.argv[3]
metedataOutFile = sys.argv[4]

#write outFile, clinical on left expression on Right


#list = []
PrimaryNameToAnnotations = {}
with open(clinicalAnnotations, 'r') as f:
    PrimaryNameToAnnotations["header"] = f.readline().strip('\n').split('\t')[1:]
    for line in f:
        lineList = line.strip('\n').split('\t')
        lineList[1] = lineList[1].replace(" ", "_")
        lineList[1] = lineList[1].replace(":", "_")
        lineList[1] = lineList[1].replace("/", "_")
        lineList[1] = lineList[1].replace("(", "_")
        lineList[1] = lineList[1].replace(")", "_")
        lineList[1] = lineList[1].replace(",", "")
        PrimaryNameToAnnotations[lineList[1]] = lineList[1:]

expressionList = []
with open(expressionData, 'r')  as inFile:
    headerList = inFile.readline().strip('\n').split('\t')
    for i in range(len(headerList)) : #Need to find the CellLinePrimaryName. This will remove the prefix and suffix
        expressionList.append([])
        if re.search(r".", headerList[i]) :
            expressionList[i].append(".".join(headerList[i].split('.')[1:-1]))
        else :
            expressionList[i].append(headerList[i])	
    for line in inFile:
        lineList = line.strip('\n').split('\t')
        if re.search(r"\|", lineList[0]):
            index = re.search(r"\|", lineList[0]).start()
            lineList[0] = lineList[0][:index]
        for i in range(len(lineList)) :
            expressionList[i].append(lineList[i])

with open(dataOutFile, 'w') as ofData:
    with open(metedataOutFile, 'w') as ofMeta: 
        first = True
        headerList = PrimaryNameToAnnotations["header"]
        for i in range(len(expressionList)) :
            try:
                if first :
                    first = False
                    ofMeta.write("Sample\tVariable\tValue\n")
                    ofData.write("Sample" + "\t" + "\t".join(expressionList[i][1:]) + "\n")
                else :
                    for j in range(len(PrimaryNameToAnnotations[expressionList[i][0]]) - 1) :
                        if PrimaryNameToAnnotations[expressionList[i][0]][j + 1] != "" :
                            ofMeta.write(PrimaryNameToAnnotations[expressionList[i][0]][0] + '\t' + headerList[j + 1] + '\t' + PrimaryNameToAnnotations[expressionList[i][0]][j + 1] + '\n')
                    ofData.write("\t".join(expressionList[i]) + "\n") 
            except KeyError: 
                 continue #This will catch the following mismatches: RS4_11, EKVX, SF539, SNB75, SF268, MOLT-3, HOP-92, HOP-62, UO-31, WM983B, HOP-62, EKVX


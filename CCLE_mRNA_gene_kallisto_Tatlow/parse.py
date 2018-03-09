import re, sys, codecs

expressionData = sys.argv[1]
clinicalAnnotations = sys.argv[2]
dataOutFile = sys.argv[3]
metedataOutFile = sys.argv[4]
drugData = sys.argv[5] 
profilingData = sys.argv[6]

#write outFile, clinical on left expression on Right

DrugDataDict = {}
with open(drugData, 'r') as f :
    firstLine = f.readline().strip('\n').strip('\r').split(',')
    DrugDataDict["Header"] = [firstLine[2], firstLine[-4], firstLine[-3], firstLine[-2], firstLine[-1]]

    for line in f :
        lineList = line.strip('\n').strip('\r').split(',')
        if lineList[1] not in DrugDataDict :
            DrugDataDict[lineList[1]] = []
        DrugDataDict[lineList[1]].append([lineList[2], lineList[-4], lineList[-3], lineList[-2], lineList[-1]])

genericToBrand = {}
with codecs.open(profilingData, 'r', "iso-8859-1") as f : 
    f.readline()
    for line in f :
        lineList = line.strip('\n').split(',')
        if lineList[1] != "" :
            brand = re.compile("(\w|-)+").search(lineList[1]).group()
            generic = re.compile("(\w|-)+").search(lineList[0]).group()

            genericToBrand[generic] = brand

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

print("organizing data")
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
            lineList[0] = lineList[0].split('|')[5] 
        present = False
        for i in range(len(expressionList[0])) :
            if expressionList[0][i] == lineList[0] :
                for j in range(len(lineList) - 1) :
                    expressionList[j + 1][i] = float(expressionList[j + 1][i]) + float(lineList[j + 1])
                present = True
                break
        if present == False :
            for i in range(len(lineList)) :
                expressionList[i].append(lineList[i])

print("writing metadata")
metadataSamples = []
with open(metedataOutFile, 'w') as ofMeta: 
    with open(expressionData, 'r')  as inFile:
        first = True
        headerList = PrimaryNameToAnnotations["header"]
        for i in range(len(expressionList)) :
            try:
                if first :
                    first = False
                    ofMeta.write("Sample\tVariable\tValue\n")
                else :
                    if expressionList[i][0] in DrugDataDict :
                        ## There is several lines of information for each cell line
                        for list in DrugDataDict[expressionList[i][0]] :
                            sample = expressionList[i][0]
                            for k in range(len(list) - 1) : 
                                ## We don't want blank vaulues or NA values.
                                if list[k + 1] == "NA" or list[k + 1] == "" :
                                    continue
                                ofMeta.write(sample + '\t' + "Drug__" + list[0] + "__" + DrugDataDict["Header"][k + 1] + '\t' + list[k + 1] + '\n')
                                ##Somtimes there are brand names. We want a duplicate with brand name info and gene info.
                                if list[0] in genericToBrand :
                                    brand = genericToBrand[list[0]]
                                    ofMeta.write(sample + '\t' + "Drug__" + brand + "__" + DrugDataDict["Header"][k + 1] + '\t' + list[k + 1] + '\n')
#                    lineList = line.strip('\n').split('\t')
                    for j in range(len(PrimaryNameToAnnotations[expressionList[i][0]]) - 1) :
                        if PrimaryNameToAnnotations[expressionList[i][0]][j + 1] != "" :
                            metadataSamples.append(PrimaryNameToAnnotations[expressionList[i][0]][0])
                            ofMeta.write(PrimaryNameToAnnotations[expressionList[i][0]][0] + '\t' + headerList[j + 1] + '\t' + PrimaryNameToAnnotations[expressionList[i][0]][j + 1] + '\n')
            except KeyError: 
                continue #This will catch the following mismatches: RS4_11, EKVX, SF539, SNB75, SF268, MOLT-3, HOP-92, HOP-62, UO-31, WM983B, HOP-62, EKVX

print("writing expression data")
with open(dataOutFile, 'w') as ofData:
    first = True
    for i in range(len(expressionList)) :
        if first :
            first = False
            ofData.write("Sample" + "\t" + "\t".join(expressionList[i][1:]) + "\n")
        else :
            if(any(str(expressionList[i][0]) == metadataSample for metadataSample in metadataSamples)) :
                ofData.write("\t".join([str(element) for element in expressionList[i]]) + "\n")

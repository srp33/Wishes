import pandas as pd
import sys, re, math, gzip
import numpy as np

cellLine = sys.argv[1]
doseResponse = sys.argv[2]
screenedComponents = sys.argv[3]
RACS = sys.argv[4]
variants = sys.argv[5]
expressionIn = sys.argv[6]
clinicalOut = sys.argv[7]
tmpExpression = sys.argv[8]
finalExpression = sys.argv[9]

def readSheetToMultipleDfs(xl,sheetname, indecisBetweenTables) :
    line = []
    previous = -1
    tmpDfsList = []
    for i in indecisBetweenTables :
        if i - previous > 2 :
            nrows = xl.book.sheet_by_name(sheetname).nrows
            df = xl.parse(sheetname, skiprows=previous+1, skip_footer = nrows-i-1).dropna(axis=1, how='all')
            tmpDfsList.append(df)
        previous = i
    return tmpDfsList

def readXlToListDf(file) :
    xl = pd.ExcelFile(file)
    dfsList = []
    for sheetname in xl.sheet_names :
        df = xl.parse(sheetname)
        if df.empty == True :
            continue
        elif any(math.isnan(s) for s in list(df[df.columns[0]]) if type(s) is float) :
            indecisBetweenTables = list(s for s in range(len(list(df[df.columns[0]]))) if type(list(df[df.columns[0]])[s]) is float)
            indecisBetweenTables.append(len(list(df[df.columns[0]])))
            tmpDfsList = readSheetToMultipleDfs(xl,sheetname,indecisBetweenTables)
            for df in tmpDfsList :
                dfsList.append(df)
        else :
            dfsList.append(df)
    return dfsList

def checkIfNan(value) :
    if type(value) == float:
        if math.isnan(value) == True:
            return True
    return False

print("making dataframes from excel")
cellLineDfs = readXlToListDf(cellLine) # 0.Cell line details 1.COSMIC tissue classification 2.TCGA tissue classification 3.Microsatillite instability data 4.Growth media
doseResponseDfs = readXlToListDf(doseResponse) # 0.fitted_dose_response
screenedComponentsDfs = readXlToListDf(screenedComponents) # 0.Screened_Compounds
RACSDfs = readXlToListDf(RACS) # 0.RACS
variantsDfs = readXlToListDf(variants) # 0.WES_variants 1.Legend


##The first three dictionaries are used to decode the MSI, Cancer type, and Screen Medium in the Cell Line file
##The fourth dictionary stores information from the DrugID in the screen compounds file to be used when making the dose response.
print("Making dictionaries")

TCGADict = {}
for i in range(len(cellLineDfs[2][cellLineDfs[2].columns[0]])) :
    TCGADict[cellLineDfs[2][cellLineDfs[2].columns[0]][i]] = cellLineDfs[2][cellLineDfs[2].columns[1]][i]

MIDDict = {}
for i in range(len(cellLineDfs[3][cellLineDfs[3].columns[0]])) :
    MIDDict[cellLineDfs[3][cellLineDfs[3].columns[0]][i]] = cellLineDfs[3][cellLineDfs[3].columns[1]][i]

GMDict = {}
for i in range(len(cellLineDfs[4][cellLineDfs[4].columns[0]])) :
    GMDict[cellLineDfs[4][cellLineDfs[4].columns[0]][i]] = cellLineDfs[4][cellLineDfs[4].columns[1]][i]

DrugIDDict = {}
for i in range(len(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[0]])) :
    drugList = []
    if (type(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i]) != float) :
        if screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i] == "-":
            if (len(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i].split(", ")) > 1) :
                drugList = screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i].split(", ")
        else :
            drugList = screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i].split(", ")
    drugList.append(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[1]][i])
    DrugIDDict[screenedComponentsDfs[0][screenedComponentsDfs[0].columns[0]][i]] = drugList

EnsembliIDDict = {}
numberOfCellLineRows = 0
for i in range(len(cellLineDfs[1][cellLineDfs[1].columns[1]])) :
    numberOfCellLineRows = numberOfCellLineRows + 1
    EnsembliIDDict[str(cellLineDfs[1][cellLineDfs[1].columns[1]][i])] = cellLineDfs[1][cellLineDfs[1].columns[0]][i]


##Write out Expression data
headersNotConverted = []
headerValues = 0
indecisOfInterest = []
headersList = []
print("Writing Expression data")
with gzip.open(expressionIn, 'r') as iF :
    with gzip.open(tmpExpression, 'w') as oF :
        headersList = iF.readline().decode().strip('\n').split('\t')

        first = True
        for i in range(len(headersList)) :
            if first == True:
                first = False
                indecisOfInterest.append(i)
            else :
                headerValues = headerValues + 1

                try :
                    headersList[i] = str(EnsembliIDDict[headersList[i]])
                    indecisOfInterest.append(i)
                except KeyError :
                    headersNotConverted.append(headersList[i])

        first = True
        firstOACp4C = True
        firstSKMEL28 = True
        firstKMH2 = True
        firstOCIAML5 = True
        for i in indecisOfInterest :
            if first == True :
                first = False
                oF.write("Sample".encode())
            elif headersList[i] == "OACp4C" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                if firstOACp4C == True :
                    firstOACp4C = False
                    continue
                else :
                    oF.write(("\t" + headersList[i]).encode())
            elif headersList[i] == "SK-MEL-28" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                if firstSKMEL28 == True :
                    firstSKMEL28 = False
                    continue
                else :
                    oF.write(("\t" + headersList[i]).encode())
            elif headersList[i] == "KM-H2" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                if firstKMH2 == True :
                    firstKMH2 = False
                    continue
                else :
                    oF.write(("\t" + headersList[i]).encode())
            elif headersList[i] == "OCI-AML5" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                if firstOCIAML5 == True :
                    firstOCIAML5 = False
                    continue
                else :
                    oF.write(("\t" + headersList[i]).encode())
            else :
                oF.write(("\t" + headersList[i]).encode())
        oF.write("\n".encode())

        j = 0
        for line in iF :
            j = j + 1
            lineList = line.decode().strip('\n').split('\t')
            first = True
            firstOACp4C = True
            firstValueOACp4C = 0
            firstSKMEL28 = True
            firstValueSKMEL28 = 0
            firstKMH2 = True
            firstValueKMH2 = 0
            firstOCIAML5 = True
            firstValueOCIAML5 = 0
            for i in indecisOfInterest :
                if first == True :
                    first = False
                    oF.write(lineList[i].encode())
                elif headersList[i] == "OACp4C" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                    if firstOACp4C == True :
                        firstOACp4C = False
                        firstValueOACp4C = float(lineList[i])
                        continue
                    else :
                        averagedValue = (firstValueOACp4C + float(lineList[i])) / 2
                        oF.write(("\t" + str(averagedValue)).encode())
                elif headersList[i] == "SK-MEL-28" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                    if firstSKMEL28 == True :
                        firstSKMEL28 = False
                        firstValueSKMEL28 = float(lineList[i])
                        continue
                    else :
                        averagedValue = (firstValueSKMEL28 + float(lineList[i])) / 2
                        oF.write(("\t" + str(averagedValue)).encode())
                elif headersList[i] == "KM-H2" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                    if firstKMH2 == True :
                        firstKMH2 = False
                        firstValueKMH2 = float(lineList[i])
                        continue
                    else :
                        averagedValue = (firstValueKMH2 + float(lineList[i])) / 2
                        oF.write(("\t" + str(averagedValue)).encode())
                elif headersList[i] == "OCI-AML5" : #The original dataset has two variables titled OACp4C, this will label only the second in the header so we can average the values on each line and leave the value in this indeci
                    if firstOCIAML5 == True :
                        firstOCIAML5 = False
                        firstValueOCIAML5 = float(lineList[i])
                        continue
                    else :
                        averagedValue = (firstValueOCIAML5 + float(lineList[i])) / 2
                        oF.write(("\t" + str(averagedValue)).encode())
                else :
                    oF.write(("\t" + str(lineList[i])).encode())
            oF.write("\n".encode())

print("number of values in header: " + str(headerValues))
print("number of cellLineRows: " + str(numberOfCellLineRows))
print("Headers not converted: " + str(headersNotConverted))


noDetailsList = []
noDoseResposeList = []
noRACSList = []
noVariants = []
keyErrorSet = set()

print("Writing Metadata")
with gzip.open(clinicalOut, 'w') as oFile :
    oFile.write("Sample\tVariable\tValue\n".encode())

    first = True
    for headerIndeci in indecisOfInterest :
        if first == True :
            first = False
            continue
        i = list(i for i in range(len(cellLineDfs[1][cellLineDfs[1].columns[0]])) if headersList[headerIndeci] == str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]))
        i = i[0]

        ##writing CellLineDetails sheet Cosmic tissue classification info
        oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[1].columns.values)[2]) + "\t" + str(cellLineDfs[1][cellLineDfs[1].columns[2]][i]) + "\n").encode())
        oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[1].columns.values)[3]) + "\t" + str(cellLineDfs[1][cellLineDfs[1].columns[3]][i]) + "\n").encode())

        ##writing CellLineDetails sheet Cell line details - 7 through 12 - map 9 - 11 on to tables in sheet Decode
        #Since they are in a different order, we need to find the index
        j = list(j for j in range(len(cellLineDfs[0][cellLineDfs[0].columns[1]]) - 1) if int(cellLineDfs[0][cellLineDfs[0].columns[1]][j]) == cellLineDfs[1][cellLineDfs[1].columns[1]][i])
        if len(j) > 0 :
            j = j[0]

            if(checkIfNan(cellLineDfs[0][cellLineDfs[0].columns[7]][j]) != True) :
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[7]).replace("\n"," ") + "\t" + str(cellLineDfs[0][cellLineDfs[0].columns[7]][j]) + "\n").encode())
            if(checkIfNan(cellLineDfs[0][cellLineDfs[0].columns[8]][j]) != True) :
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[8]).replace("\n"," ") + "\t" + str(cellLineDfs[0][cellLineDfs[0].columns[8]][j]) + "\n").encode())
            if(checkIfNan(cellLineDfs[0][cellLineDfs[0].columns[9]][j]) != True) :
                try :
                    oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[9]).replace("\n"," ") + "\t" + str(TCGADict[cellLineDfs[0][cellLineDfs[0].columns[9]][j]]) + "\n").encode())
                except KeyError :
                    if (cellLineDfs[0][cellLineDfs[0].columns[9]][j] == "COAD/READ") :
                        oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[9]).replace("\n"," ") + "\t" + "Colon adenocarcinoma and Rectum adenocarcinoma" + "\n").encode())
                    else :
                        keyErrorSet.add(cellLineDfs[0][cellLineDfs[0].columns[9]][j])
            if(checkIfNan(cellLineDfs[0][cellLineDfs[0].columns[10]][j]) != True) :
                tmpMIS = cellLineDfs[0][cellLineDfs[0].columns[10]][j].split('/')
                tmpMIS = list(MIDDict[i] for i in tmpMIS)
                tmpMIS = "/".join(tmpMIS)
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[10]).replace("\n"," ") + "\t" + str(tmpMIS) + "\n").encode())
            if(checkIfNan(cellLineDfs[0][cellLineDfs[0].columns[11]][j]) != True) :
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[11]).replace("\n"," ") + "\t" + str(GMDict[cellLineDfs[0][cellLineDfs[0].columns[11]][j]]) + "\n").encode())
            if(checkIfNan(cellLineDfs[0][cellLineDfs[0].columns[12]][j]) != True) :
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + str(list(cellLineDfs[0].columns.values)[12]).replace("\n"," ") + "\t" + str(cellLineDfs[0][cellLineDfs[0].columns[12]][j]) + "\n").encode())
        else :
            noDetailsList.append(i)

        ##Writing dose response
        j = list(j for j in range(len(doseResponseDfs[0][doseResponseDfs[0].columns[2]])) if doseResponseDfs[0][doseResponseDfs[0].columns[2]][j] == cellLineDfs[1][cellLineDfs[1].columns[1]][i])

        if(len(j) > 0) :
            for k in j :
                drugList = DrugIDDict[doseResponseDfs[0][doseResponseDfs[0].columns[3]][k]]

                for drug in drugList :
                    oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + "Drug_" + str(drug) + "_" + str(list(doseResponseDfs[0].columns.values)[4]) + "\t" + str(doseResponseDfs[0][doseResponseDfs[0].columns[4]][k]) + "\n").encode())
                    oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + "Drug_" + str(drug) + "_" + str(list(doseResponseDfs[0].columns.values)[5]) + "\t" + str(doseResponseDfs[0][doseResponseDfs[0].columns[5]][k]) + "\n").encode())
                    oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + "Drug_" + str(drug) + "_" + str(list(doseResponseDfs[0].columns.values)[6]) + "\t" + str(doseResponseDfs[0][doseResponseDfs[0].columns[6]][k]) + "\n").encode())
                    oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + "Drug_" + str(drug) + "_" + str(list(doseResponseDfs[0].columns.values)[7]) + "\t" + str(doseResponseDfs[0][doseResponseDfs[0].columns[7]][k]) + "\n").encode())
        else :
            noDoseResposeList.append(i)

        ##Writing Racs
        j = list(j for j in range(len(RACSDfs[0][RACSDfs[0].columns[1]])) if RACSDfs[0][RACSDfs[0].columns[1]][j] == cellLineDfs[1][cellLineDfs[1].columns[1]][i])

        if (len(j)) > 0 :
            for k in j :
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + "RACS_" + str(RACSDfs[0][RACSDfs[0].columns[5]][k]) + "\t" + str(RACSDfs[0][RACSDfs[0].columns[6]][k]) + "\n").encode())
        else :
            noRACSList.append(i)

        ##Writing WES_Variants
        j = list(j for j in range(len(variantsDfs[0][variantsDfs[0].columns[1]])) if variantsDfs[0][variantsDfs[0].columns[1]][j] == cellLineDfs[1][cellLineDfs[1].columns[1]][i])

        if len(j) > 0 :
            for k in j :
                oFile.write((str(cellLineDfs[1][cellLineDfs[1].columns[0]][i]) + "\t" + "Variant_" + str(variantsDfs[0][variantsDfs[0].columns[7]][k]) + "\t" +  str(variantsDfs[0][variantsDfs[0].columns[3]][k]) + "\n").encode())
        else :
            noVariants.append(i)


print("KeyError result: " + str(keyErrorSet))
print("Iterations no details: " + str(noDetailsList))
print("Iterations no racs info: " + str(noRACSList))
print("Iterations no variants info: " + str(noVariants))
print("Iterations no Dose Response: " + str(noDoseResposeList))

print("transpose the expressionFile")
with gzip.open(tmpExpression, 'r') as f :
    with gzip.open(finalExpression, 'w') as oF :
        data = np.genfromtxt(f,delimiter='\t',dtype=str)
        for line in data.T :
            stringLine = ("\t").join([str(element) for element in line]) + "\n"
            oF.write(stringLine.encode())

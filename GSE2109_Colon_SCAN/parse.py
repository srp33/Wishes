import sys, gzip

clinicalInfo = sys.argv[1]
expressionInfo = sys.argv[2]
dataOutFile = sys.argv[3]
metedataOutFile = sys.argv[4]

#Rows don't match, so need to match them
with open(expressionInfo, 'r')  as f1:
    with open(clinicalInfo, 'r') as f2:
        with open(metedataOutFile, 'w') as ofMeta:
            with open(dataOutFile, 'w') as ofNorm:
                file1List = f1.read().splitlines()
                file2List = f2.read().splitlines()
                file1IDSet = set()
                for index in range(len(file1List)) :
                    lineFile1List = file1List[index].strip('\n').split('\t')
                    file1IDSet.add(lineFile1List[0])

                rowsOfInterest2 = [i for i in range(len(file2List))  if file2List[i].strip('\n').split('\t')[0] in file1IDSet]
                
                ofMeta.write("Sample\tVariable\tValue\n")                
#                ofMeta.write(lineList[0] + '\t' + headerList[1] + '\t' + lineList[1] + '\n')
                headerList = file2List[0].strip('\n').split('\t')
                ofNorm.write("Sample" + '\t' + '\t'.join(file1List[0].strip('n').split('\t')[1:]) + '\n')
#                f3.write(file2List[0] + '\t' + '\t'.join(file1List[0].strip('\n').split('\t')[1:])+ '\n')
                for index in range(len(rowsOfInterest2)):
#                    f3.write(file2List[rowsOfInterest2[index]] + '\t' + '\t'.join(file1List[index + 1].strip('\n').split('\t')[1:]) + '\n')
                    lineList = file2List[rowsOfInterest2[index]].strip('\n').split('\t')
                    for index2 in range(len(lineList) - 1) :
                        if(lineList[index2 + 1] != "NA") :
                            ofMeta.write(lineList[0] + '\t' + headerList[index2 + 1] + '\t' + lineList[index2 + 1] + '\n')
                    ofNorm.write(file1List[index + 1] + '\n')

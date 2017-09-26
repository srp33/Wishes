import sys, gzip

clinicalInfo = sys.argv[1]
expressionInfo = sys.argv[2]
outFile = sys.argv[3]

#Rows don't match, so need to match them
with open(expressionInfo, 'r')  as f1:
    with open(clinicalInfo, 'r') as f2:
        with open(outFile, 'w') as f3:
            file1List = f1.read().splitlines()
            file2List = f2.read().splitlines()
            file1IDSet = set()
            for index in range(len(file1List)) :
                lineFile1List = file1List[index].strip('\n').split('\t')
                file1IDSet.add(lineFile1List[0])
            rowsOfInterest2 = [i for i in range(len(file2List))  if file2List[i].strip('\n').split('\t')[0] in file1IDSet]
            f3.write(file2List[0] + '\t' + '\t'.join(file1List[0].strip('\n').split('\t')[1:])+ '\n')
            for index in range(len(rowsOfInterest2)):
                f3.write(file2List[rowsOfInterest2[index]] + '\t' + '\t'.join(file1List[index + 1].strip('\n').split('\t')[1:]) + '\n')

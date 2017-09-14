import sys, gzip

expressionData = sys.argv[1]
clinicalData = sys.argv[2]
outFile = sys.argv[3]

with open(expressionData, 'r')  as f1:
    with open(clinicalData, 'r') as f2:
        with open(outFile, 'w') as f3:
            file1List = f1.read().splitlines()
            file2List = f2.read().splitlines()
            for index in range(len(file1List)) :
                lineFile1List = file1List[index].strip('\n').split('\t')
                lineFile2List = file2List[index].strip('\n').split('\t')
                f3.write('\t'.join(lineFile2List) + '\t' + '\t'.join(lineFile1List[1:]) + '\n')
#                if (index == 0) :
#                    print(lineFile1List[1])    
#                else: 
#                    if (lineFile1List[0] != lineFile2List[0]) :
#                        print('problem')
#                    else :
#                        print('success')

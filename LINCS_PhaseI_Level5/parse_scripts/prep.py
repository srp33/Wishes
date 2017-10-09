import pandas as pd
import sys, gzip

adjustedFile = sys.argv[1]
gctxFileName = sys.argv[2]
parallelFile = sys.argv[3]
metaOutFilePrefix = sys.argv[4] 
expressionDataOutFilePrefix = sys.argv[5]
tmpFile = sys.argv[6]
geneFile = sys.argv[7]
expressionDataFinal = sys.argv[8]
metaDataFinal = sys.argv[9]

#Makes Sig_info panda dataframe
sig_info = pd.read_csv(adjustedFile, dtype={'sig_id': str, 'pert_id': str, 'pert_iname': str, 'pert_type': str, 'cell_id': str, 'pert_dose': float, 'pert_dose_unit': str, 'pert_idose': str, 'pert_time': str, 'pert_time_unit': str, 'pert_itime': str}, sep="\t", na_filter=False, low_memory=True)

del sig_info['distil_id']
list_sig_id = list(sig_info["sig_id"].unique())

#Makes a dataframe that is written to the tmpFile. This tmpFile is used to read the headers
cell_id = sig_info["sig_id"][sig_info["sig_id"] == "AML001_CD34_24H:A05"]

from cmapPy.pandasGEXpress import parse
cell_id_only_gctoo = parse(gctxFileName, cid=cell_id)
transposed_df = cell_id_only_gctoo.data_df.T
transposed_df.insert(0, 'sig_id', transposed_df.index)
result = pd.merge(sig_info, transposed_df, on='sig_id')

result.to_csv(tmpFile, header=True, index=False, sep='\t')

#parses the document that reads geneId to gene Name, this is used to write out expression header
geneDict = {}
with gzip.open(geneFile, 'r') as f :
    headerLine = f.readline()

    for line in f :
        list = line.strip('\n').split('\t')
        geneDict[list[0]] = list[1]

#uses created data frame to write out Expression Data headerline and make the headerList to be used in parallel
headerList = []
with open(tmpFile, 'r') as f :
    with gzip.open(expressionDataFinal, 'w') as ofExpression :
        firstLine = f.readline()
        list = firstLine.strip('\n').split('\t')
        ofExpression.write("Sample")
        for element in list :
            if element in geneDict.keys():
                ofExpression.write('\t' + geneDict[element])
            else :
                headerList.append(element)
        ofExpression.write('\n')


#Writes out First line of MetaDataFinal
with gzip.open(metaDataFinal, 'w') as ofMeta :
    ofMeta.write("Sample\tVariable\tValue\n")

#Writes the commands that will be executed in parallel

with open(parallelFile, 'w') as f :
    amount = 0
    list = []
    for element_sig_id in list_sig_id:
        list.append(element_sig_id)
        if len(list) > 1000 :
            amount = amount + 1
            f.write("python parse_scripts/processSigID.py " + str(amount)+ " " + gctxFileName + " " + adjustedFile + " " + metaOutFilePrefix + str(amount) + ".csv.gz " + expressionDataOutFilePrefix + str(amount) + ".csv.gz \"" + ' '.join(headerList) + "\"\n")
            list = []
    f.write("python parse_scripts/processSigID.py " + str(amount + 1)+ " " + gctxFileName + " " + adjustedFile + " " + metaOutFilePrefix + str(amount + 1) + ".csv.gz " + expressionDataOutFilePrefix + str(amount + 1) + ".csv.gz \"" + ' '.join(headerList) + "\"\n")


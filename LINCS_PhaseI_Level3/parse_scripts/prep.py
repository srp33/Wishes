import pandas as pd
import sys, gzip

instInfoFile = sys.argv[1]
gctxFileName = sys.argv[2]
parallelFile = sys.argv[3]
metaOutFilePrefix = sys.argv[4]
expressionDataOutFilePrefix = sys.argv[5]
tmpFile = sys.argv[6]
geneFile = sys.argv[7]
expressionDataFinal = sys.argv[8]
metaDataFinal = sys.argv[9]

#Makes inst_info dataframe
inst_info = pd.read_csv(instInfoFile, dtype={'inst_id': str, 'rna_plate': str, 'rna_well': str, 'pert_id': str, 'pert_iname': str, 'pert_type': str, 'pert_dose': float, 'pert_dose_unit': str, 'pert_time': float, 'pert_time_unit': str, 'cell_id': str}, sep="\t", na_filter=False, low_memory=True)

list_inst_id = list(inst_info["inst_id"].unique())

#Makes a datafram that is written to the tmpFile.This tmpFile is used to read the headers
cell_id = inst_info["inst_id"][inst_info["inst_id"] == "ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13"]

from cmapPy.pandasGEXpress import parse
cell_id_only_gctoo = parse(gctxFileName, cid=cell_id)
transposed_df = cell_id_only_gctoo.data_df.T
transposed_df.insert(0, 'inst_id', transposed_df.index)
result = pd.merge(inst_info, transposed_df, on='inst_id')

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
    list = []
    amount = 0
    for element_inst_id in list_inst_id:
        list.append(element_inst_id)
        if len(list) > 1000:
            amount = amount + 1
            f.write("python parse_scripts/processInstID.py " + str(amount) + " " + gctxFileName + " " + instInfoFile + " " + metaOutFilePrefix + str(amount) + ".csv.gz " + expressionDataOutFilePrefix + str(amount) + ".csv.gz \"" + ' '.join(headerList) + "\"\n")
            list = []
    f.write("python parse_scripts/processInstID.py " + str(amount + 1) + " " + gctxFileName + " " + instInfoFile + " " + metaOutFilePrefix + str(amount + 1) + ".csv.gz " + expressionDataOutFilePrefix + str(amount + 1) + ".csv.gz \"" + ' '.join(headerList) + "\"\n")

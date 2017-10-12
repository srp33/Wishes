import pandas as pd
import sys, gzip

iteration = sys.argv[1]
gctxFileName = sys.argv[2]
instInfoFile = sys.argv[3]
metaDataOutFile = sys.argv[4]
expressionDataOutFile = sys.argv[5]
headerList = sys.argv[6].split(' ')

print("Processing group " + iteration)

inst_info = pd.read_csv(instInfoFile, dtype={'inst_id': str, 'rna_plate': str, 'rna_well': str, 'pert_id': str, 'pert_iname': str, 'pert_type': str, 'pert_dose': float, 'pert_dose_unit': str, 'pert_time': float, 'pert_time_unit': str, 'cell_id': str}, sep="\t", na_filter=False, low_memory=True)

if (int(iteration) != 1318) :
    start = 1000 * (int(iteration) - 1)
    finish = 1000 * int(iteration)
else :
    start = 1000 * (int(iteration) - 1)
    finish = start + 821 

inst_id =  inst_info["inst_id"][start:finish]

from cmapPy.pandasGEXpress import parse
inst_id_only_gctoo = parse(gctxFileName, cid = inst_id)
transposed_df = inst_id_only_gctoo.data_df.T
transposed_df.insert(0, 'inst_id', transposed_df.index)
transposed_df.to_csv(expressionDataOutFile, header=False, index=False, sep='\t', compression='gzip')

inst_info_Specific_Iteration = inst_info[start:finish]
instSpecificList = []

for row in inst_info_Specific_Iteration.iterrows() :
    index, data = row
    instSpecificList.append(data.tolist())

with gzip.open(metaDataOutFile, 'w') as ofMeta :
    for row in instSpecificList :
        for i in range(len(headerList) - 1) :
            if(str(row[i + 1]) != "-666") :
                ofMeta.write(str(row[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(row[i + 1]) + '\n')

print("Finished writing group " + iteration)


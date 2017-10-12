import pandas as pd
import sys, gzip

iteration = sys.argv[1]
gctxFileName = sys.argv[2]
adjustedFile = sys.argv[3]
metaDataOutFile = sys.argv[4]
expressionDataOutFile = sys.argv[5]
headerList = sys.argv[6].split(' ')

print("Processing group " + iteration)
sig_info = pd.read_csv(adjustedFile, dtype={'sig_id': str, 'pert_id': str, 'pert_iname': str, 'pert_type': str, 'cell_id': str, 'pert_dose': float, 'pert_dose_unit': str, 'pert_idose': str, 'pert_time': str, 'pert_time_unit': str, 'pert_itime': str}, sep="\t", na_filter=False, low_memory=True)

del sig_info['distil_id']

if (int(iteration) != 188) :
    start = 200 * (int(iteration) - 1)
    finish = 200 * int(iteration) 
else :
    start = 200 * (int(iteration) - 1)
    finish = start + 933 

sig_id = sig_info["sig_id"][start:finish]

from cmapPy.pandasGEXpress import parse
sig_id_only_gctoo = parse(gctxFileName, cid=sig_id)
transposed_df = sig_id_only_gctoo.data_df.T
transposed_df.insert(0, 'sig_id', transposed_df.index)
transposed_df.to_csv(expressionDataOutFile, header=False, index=False, sep='\t', compression='gzip')

sig_info_Specific_Iteration = sig_info[start:finish]
sigSpecificList = []

for row in sig_info_Specific_Iteration.iterrows() :
    index, data = row
    sigSpecificList.append(data.tolist())

with gzip.open(metaDataOutFile, 'w') as ofMeta :
    for row in sigSpecificList :
        for i in range(len(headerList) - 1) :
            if(str(row[i + 1]) != "-666") :
                ofMeta.write(str(row[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(row[i + 1]) + '\n')

print("Finished writing group " + iteration)

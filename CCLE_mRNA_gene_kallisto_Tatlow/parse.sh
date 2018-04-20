#! /bin/bash

redirectedTempFolder=tmp
expressionData=$redirectedTempFolder/CCLE_tpm_Expression.tsv
clinicalAnnotations=$redirectedTempFolder/CCLE_tpm_Clinical.tsv
drugData=$redirectedTempFolder/CCLE_NP24.2009_Drug_data_2015.02.24.csv
profilingData=$redirectedTempFolder/CCLE_NP24.2009_profiling_2012.02.20.csv
data1=$redirectedTempFolder/CCLE_copynumber_byGene_2013-12-03.txt
meta2=$redirectedTempFolder/ccle2maf_20170805f.txt
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz
#Make sure old files are deleted#Make sure old files are deleted
rm -f $metadataOutFilegz
rm -f $dataOutFilegz

python parse.py $expressionData $clinicalAnnotations $dataOutFile $metadataOutFile $drugData $profilingData

gzip $metadataOutFile
gzip $dataOutFile

python3 parseData1.py $data1 $dataOutFilegz
python3 parseMeta2.py $meta2 $metadataOutFilegz
python3 keep_common_samples.py $metadataOutFilegz $dataOutFilegz

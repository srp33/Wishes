#! /bin/bash

redirectedTempFolder=tmp
expressionData=$redirectedTempFolder/CCLE_tpm_Expression.tsv
clinicalAnnotations=$redirectedTempFolder/CCLE_tpm_Clinical.tsv
drugData=$redirectedTempFolder/CCLE_NP24.2009_Drug_data_2015.02.24.csv  
profilingData=$redirectedTempFolder/CCLE_NP24.2009_profiling_2012.02.20.csv
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz
convertedMetaOut=Clinical.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz

python3 parse.py $expressionData $clinicalAnnotations $dataOutFile $metadataOutFile $drugData $profilingData

gzip $metadataOutFile
gzip $dataOutFile

python3 convertTallFormatToWide.py $metadataOutFilegz $convertedMetaOut

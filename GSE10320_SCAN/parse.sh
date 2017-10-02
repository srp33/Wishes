#! /bin/bash

redirectedTempFolder=tmp
expressionData=$redirectedTempFolder/GSE10320_SCAN_Expression
clinicalData=$redirectedTempFolder/GSE10320_SCAN_Clinical
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz
#execute
python parse.py $expressionData $clinicalData $dataOutFile $metadataOutFile 

#clean-up
rm -f .gitignore
echo $dataOutFilegz >> .gitignore
echo $metadataOutFilegz >> .gitignore
echo $redirectedTempFolder >> .gitignore
#rm -r $redirectedTempFolder

gzip $metadataOutFile
gzip $dataOutFile

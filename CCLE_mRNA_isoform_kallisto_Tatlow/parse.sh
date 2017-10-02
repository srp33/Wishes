#! /bin/bash

redirectedTempFolder=tmp
expressionData=$redirectedTempFolder/CCLE_tpm_Expression.tsv
clinicalAnnotations=$redirectedTempFolder/CCLE_tpm_Clinical.tsv
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz
#execute
python parse.py $expressionData $clinicalAnnotations $dataOutFile $metadataOutFile

#clean-up
rm -f .gitignore
echo $dataOutFilegz >> .gitignore
echo $metadataOutFilegz >> .gitignore
echo $redirectedTempFolder >> .gitignore
rm -rf $redirectedTempFolder

gzip $metadataOutFile
gzip $dataOutFile

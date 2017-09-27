#! /bin/bash

redirectedTempFolder=tmp
Expression=$redirectedTempFolder/GSE2109_Colon_SCAN_Expression
Clinical=$redirectedTempFolder/GSE2109_Colon_SCAN_Clinical
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz
#execute
python parse.py $Clinical $Expression $dataOutFile $metadataOutFile 

#clean-up
rm -f .gitignore
echo $dataOutFilegz >> .gitignore
echo $metadataOutFilegz >> .gitignore
echo $redirectedTempFolder >> .gitignore
rm -r $redirectedTempFolder

gzip $metadataOutFile
gzip $dataOutFile

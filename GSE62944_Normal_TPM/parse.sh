#! /bin/bash

redirectedTempFolder=tmp
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt.gz
NormalTPM=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_TPM.txt.gz
nameToAbbreviation="nameToAbbreviation.txt"
dataOutFile=Gene_Expression.tsv
metadataOutFile=metadata.tsv
metadataOutFileTranslated=Clinical.tsv

python parse.py $PatientCancerType $NormalTPM $dataOutFile $metadataOutFile $nameToAbbreviation
python3 ../Helper/convertTallFormatToWide2.py $metadataOutFile $metadataOutFileTranslated
rm -r $metadataOutFile

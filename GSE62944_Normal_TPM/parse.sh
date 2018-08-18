#! /bin/bash

redirectedTempFolder=tmp
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt.gz
NormalTPM=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_TPM.txt.gz
nameToAbbreviation="nameToAbbreviation.txt"
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz
metadataOutFileTranslated=Clinical.tsv.gz

python parse.py $PatientCancerType $NormalTPM $dataOutFilegz $metadataOutFilegz $nameToAbbreviation
python3 convertTallFormatToWide.py $metadataOutFilegz $metadataOutFileTranslated
rm -r $metadataOutFilegz

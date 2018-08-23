#! /bin/bash

set -o errexit

redirectedTempFolder=tmp
metaData=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz
patientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz
tumorFeatureCounts=$redirectedTempFolder/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_FeatureCounts.txt.gz
nameToAbbreviation=nameToAbbreviation.txt
dataOut=Gene_Expression.tsv.gz
metadataOut=metadata.tsv.gz
metadataTranslated=Clinical.tsv.gz

python parse.py $metaData $patientCancerType $tumorFeatureCounts $dataOut $metadataOut $nameToAbbreviation
python convertTallFormatToWide.py $metadataOut $metadataTranslated
rm -f $metadataOut

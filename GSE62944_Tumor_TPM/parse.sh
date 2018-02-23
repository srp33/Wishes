#! /bin/bash

redirectedTempFolder=tmp
metaData=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz
patientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz
tumorTPM=$redirectedTempFolder/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz
tcgaHtml=$redirectedTempFolder/"tcga_abbreviations.html"
nameToAbbreviation=$redirectedTempFolder/"nameToAbbreviation.txt"
dataOut=data.tsv.gz
metadataOut=metadata.tsv.gz

source activate WishBuilderDependencies

Rscript scrapeWebTCGA.R $tcgaHtml $nameToAbbreviation
python parse.py $metaData $patientCancerType $tumorTPM $dataOut $metadataOut $nameToAbbreviation


#! /bin/bash

python3 ParseCancerType.py tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz nameToAbbreviation.txt tmp/Clinical.tsv
python3 ParseClinical.py tmp/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz tmp/Clinical.tsv
python3 ../Helper/convertTallFormatToWide2.py tmp/Clinical.tsv.gz Clinical.tsv

python3 TransposeData.py tmp/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz tmp/Gene_Expression.tsv
python3 SetFirstColumnHeader.py tmp/Gene_Expression.tsv Sample Gene_Expression.tsv

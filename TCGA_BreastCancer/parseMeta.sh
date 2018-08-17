#! /bin/bash/

patientCancerType=tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz
clinicalData=tmp/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz
abbreviationFile=cancerTypeAbbreviations.tsv

python3 parseCancerTypes.py $patientCancerType $abbreviationFile tmp/Clinical.tsv.gz
python3 parseClinical.py $clinicalData tmp/Clinical.tsv.gz

#Convert Clinical from tall format to wide
python3 convertTallFormatToWide.py tmp/Clinical.tsv.gz Clinical.tsv.gz

#Leave only breast cancer samples
python3 onlyBreastCancer.py Clinical.tsv.gz breastClinical.tsv.gz

#Remove any variables with redundant value for all samples (i.e. SEX, FEMALE)
python3 cleanClinical.py breastClinical.tsv.gz Clinical.tsv.gz


rm -f breastClinical.tsv.gz



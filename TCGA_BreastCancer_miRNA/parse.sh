#! /bin/bash

#SBATCH --time=05:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core
#source activate WishBuilderDependencies

miRNAdata=tmp/miRNA_HiSeq_gene.gz
patientCancerType=tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz
clinicalData=tmp/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz
abbreviationFile=cancerTypeAbbreviations.tsv

python3 parseData.py $miRNAdata miRNA.tsv.gz
python3 parseCancerTypes.py $patientCancerType $abbreviationFile tmp/Clinical.tsv.gz
python3 parseClinical.py $clinicalData tmp/Clinical.tsv.gz
#python3 parseClinical.py tmp/cleanClinical.tsv.gz tmp/Clinical.tsv.gz

############################################
# Write a script that removes variables from tmp/Clinical.tsv.gz
# that have all the same value for a given variable.
############################################
# Instead of keep_common_samples.py, remove any sample from Clinical.tsv.gz that
# is not a breast cancer sample.
# When you work with gene-expression (future), filter that to only
# include data from breast cancer patients.
############################################

#Convert Clinical from tall format to wide
python3 convertTallFormatToWide.py tmp/Clinical.tsv.gz Clinical.tsv.gz

#Leave only breast cancer samples
python3 onlyBreastCancer.py Clinical.tsv.gz breastClinical.tsv.gz

#Remove any variables with redundant value for all samples (i.e. SEX, FEMALE)
python3 cleanClinical.py breastClinical.tsv.gz Clinical.tsv.gz


rm -f breastClinical.tsv.gz


#python3 keep_common_samples.py miRNA.tsv.gz tmp/Clinical.tsv.gz
#python3 convertTallFormatToWide.py tmp/Clinical.tsv.gz Clinical.tsv.gz
#source deactivate WishBuilderDependencies

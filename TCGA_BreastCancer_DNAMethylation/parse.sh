#! /bin/bash

#SBATCH --time=05:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core
#source activate WishBuilderDependencies
set -o errexit
#Folders
redirectedTemp=tmp

#InFile
patientCancerType=$redirectedTemp/"GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt"

#OutFile
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

Rscript parse.R
python3 parseMeta.py $patientCancerType $metadataOutFilegz

gzip $dataOutFilegz
gzip $metadataOutFilegz

#python3 keep_common_values.py "metadata.tsv.gz" "data.tsv.gz"
#source deactivate WishBuilderDependencies

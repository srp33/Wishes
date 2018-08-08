#! /bin/bash

#SBATCH --time=05:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core
#source activate WishBuilderDependencies

#Folders
redirectedTemp=tmp

#InFile
CNVdata=$redirectedTemp/"Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes"
patientCancerType=$redirectedTemp/"GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt"

#OutFile
dataOutFilegz=data.tsv
metadataOutFilegz=metadata.tsv
convertedMetaOut=Clinical.tsv.gz
#Values is a file previously created by matches.py that contains the common samples of data and metadata
commonValues=values

#source activate WishBuilderDependencies

#python3 matches.py $CNVdata $patientCancerType $commonValues
python3 parseData.py $CNVdata $dataOutFilegz
python3 parseMeta.py $patientCancerType $commonValues $metadataOutFilegz


gzip $dataOutFilegz
gzip $metadataOutFilegz


#To insure only common samples
python3 keep_common_samples.py "metadata.tsv.gz" "data.tsv.gz"

#Conversion of metadata to wide format
python3 convertTallFormatToWide.py "metadata.tsv.gz" $convertedMetaOut
#source deactivate WishBuilderDependencies

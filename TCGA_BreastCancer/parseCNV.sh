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

#OutFile
dataOutFilegz=CNV.tsv
#Values is a file previously created by matches.py that contains the common samples of data and metadata
commonValues=values

#source activate WishBuilderDependencies

#python3 matches.py $CNVdata $patientCancerType $commonValues
python3 parseData.py $CNVdata CNV.tsv.gz


#source deactivate WishBuilderDependencies

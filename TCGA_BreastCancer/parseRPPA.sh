#! /bin/bash

#SBATCH --time=05:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core
#source activate WishBuilderDependencies

#Folders
redirectedTemp=tmp

#InFile
RPPAdata=$redirectedTemp/"TCGA.BRCA.sampleMap"

python3 parseData.py $RPPAdata RPPA.tsv.gz

#source deactivate WishBuilderDependencies

#!/bin/bash

#SBATCH --time=20:00:00   # walltime
#SBATCH --ntasks=8   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=32768M   # memory per CPU core

#Directory variables
redirectedTempFolder=tmp
softwareFolder=Software

#Downloaded in download.sh
sigFileName=$redirectedTempFolder/GSE92742_Broad_LINCS_sig_info.txt.gz
sig_metrics=$redirectedTempFolder/GSE92742_Broad_LINCS_sig_metrics.txt.gz
gctxFileName=$redirectedTempFolder/LINCS_PhaseI_Level5.gctx
geneFile=$redirectedTempFolder/GSE92742_Broad_LINCS_gene_info.txt.gz
cellInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_cell_info.txt.gz
pertInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_info.txt.gz
pertMetrics=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_metrics.txt.gz

#Will Create
dataOutFile=data.tsv.gz
metadataOutFile=metadata.tsv.gz

#miniconda is used to store panda software in environments need to activate environment
echo "Setting up environment"
#source activate WishBuilderDependencies2
source activate lincs_env 

python2 parse.py $sigFileName $gctxFileName $metadataOutFile $dataOutFile $geneFile $cellInfo $pertInfo $pertMetrics $sig_metrics

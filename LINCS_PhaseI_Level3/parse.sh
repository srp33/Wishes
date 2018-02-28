#!/bin/bash

#SBATCH --time=8:00:00   # walltime
#SBATCH --ntasks=8   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=32768M   # memory per CPU core

#Directory variables
redirectedTempFolder=tmp
softwareFolder=Software

#Downloaded in download.sh
instInfoFileName=$redirectedTempFolder/GSE92742_Broad_LINCS_inst_info.txt.gz
gctxFileName=$redirectedTempFolder/LINCS_PhaseI_Level3.gctx
geneFile=$redirectedTempFolder/GSE92742_Broad_LINCS_gene_info.txt.gz

#Downloaded and Installed in install.sh
minicondaPath=$softwareFolder/miniconda/bin/

#Will Create
dataOutFile=data.tsv.gz
metadataOutFile=metadata.tsv.gz

#Other Metadata files that are included in final output
cellInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_cell_info.txt.gz
pertInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_info.txt.gz	
pertMetrics=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_metrics.txt.gz

#miniconda is used to store panda software in environments need to activate environment
#source activate WishBuilderDependencies2
source activate lincs_env

python3 parse.py $instInfoFileName $gctxFileName $metadataOutFile $dataOutFile $geneFile $cellInfo $pertInfo $pertMetrics 

#!/bin/bash

#SBATCH --time=15:00:00   # walltime
#SBATCH --ntasks=8   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=32768M   # memory per CPU core

#Directory variables
redirectedTempFolder=tmp
createdFilesFolder=$redirectedTempFolder/Files_Created
metaDataOutFiles=$createdFilesFolder/Meta_Data
expressionDataOutFiles=$createdFilesFolder/Expression_Data
softwareFolder=Software

#Downloaded in download.sh
instInfoFileName=$redirectedTempFolder/GSE92742_Broad_LINCS_inst_info.txt.gz
gctxFileName=$redirectedTempFolder/LINCS_PhaseI_Level3.gctx
geneFile=$redirectedTempFolder/GSE92742_Broad_LINCS_gene_info.txt.gz

#Downloaded and Installed in install.sh
parallelCommand=$softwareFolder/parallel-20170822/src/parallel
minicondaPath=$softwareFolder/miniconda/bin/

#Will create
parallelFile=$createdFilesFolder/LINCS_PhaseI_Level3_parallel.txt
metaDataOutFilePrefix=$metaDataOutFiles/LINCS_PhaseI_Level5_inst_id_group_metadata_
expressionDataOutFilePrefix=$expressionDataOutFiles/LINCS_PhaseI_Level3_inst_id_group_expression_data_
tmpHeaderFile=$createdFilesFolder/header.txt
dataOutFile=data.tsv.gz
metadataOutFile=$createdFilesFolder/tmp_metadata.tsv.gz
finalMetadataOutFile=metadata.tsv.gz

#Other Metadata files that are included in final output
cellInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_cell_info.txt.gz
pertInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_info.txt.gz
pertMatrics=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_metrics.txt.gz

rm -f $finalMetadataOutFile
rm -f $dataOutFile

#Create createdFilesFolder
mkdir -p $createdFilesFolder
rm -rf $createdFilesFolder/*
mkdir -p $metaDataOutFiles
mkdir -p $expressionDataOutFiles

#miniconda is used to store panda software in environments need to activate environment
echo "Setting up environment"
cd $minicondaPath
source activate my_cmapPy_env
cd ../../..

#Creates the parallel execution File
echo "Preparing for parallel execution"
python parse_scripts/prep.py $instInfoFileName $gctxFileName $parallelFile $metaDataOutFilePrefix $expressionDataOutFilePrefix $tmpHeaderFile $geneFile $dataOutFile $metadataOutFile

#Executes in Parallel
echo "parallel executing"
$parallelCommand --jobs 8 --tmpdir $redirectedTempFolder < $parallelFile

#Merges files that were created in Parallel
echo "merging"
cat $expressionDataOutFilePrefix* >> $dataOutFile
cat $metaDataOutFilePrefix* >> $metadataOutFile

#Expands metadata.tsv.gz with files GSE92742_Broad_LINCS_cell_info.txt.gz, GSE92742_Broad_LINCS_pert_info.txt.gz, and GSE92742_Broad_LINCS_pert_metrics.txt.gz
echo "matching additional metadata info to metadata.tsv.gz"
python parse_scripts/adjustMetadata.py $metadataOutFile $finalMetadataOutFile $cellInfo $pertInfo $pertMatrics

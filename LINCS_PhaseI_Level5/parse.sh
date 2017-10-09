#!/bin/bash

#SBATCH --time=5:00:00   # walltime
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
sigFileName=$redirectedTempFolder/GSE92742_Broad_LINCS_sig_info.txt.gz
gctxFileName=$redirectedTempFolder/LINCS_PhaseI_Level5.gctx
geneFile=$redirectedTempFolder/GSE92742_Broad_LINCS_gene_info.txt.gz

#Downloaded and Installed in install.sh
minicondaPath=$softwareFolder/miniconda/bin/
parallelCommand=$softwareFolder/parallel-20170822/src/parallel

#Will Create
tempSigFileName=$createdFilesFolder/GSE92742_Broad_LINCS_sig_info_adjusted.txt.gz
parallelFile=$createdFilesFolder/LINCS_PhaseI_Level5_parallel.txt
metaDataOutFilePrefix=$metaDataOutFiles/LINCS_PhaseI_Level5_sig_id_group_metadata_
expressionDataOutFilePrefix=$expressionDataOutFiles/LINCS_PhaseI_Level5_sig_id_group_expression_data_
tmpHeaderFile=$createdFilesFolder/header.txt
dataOutFile=data.tsv.gz
metadataOutFile=$createdFilesFolder/tmp_metadata.tsv.gz
finalMetadataOutFile=metadata.tsv.gz

#Other Metadata files that are included in final output
cellInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_cell_info.txt.gz
pertInfo=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_info.txt.gz
pertMatrics=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_metrics.txt.gz

rm -f $metadataOutFile
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

#Change format of Sig_info
echo "Creating adjusted sig info file"
python parse_scripts/adjust_sig_info.py $sigFileName $tempSigFileName

#Creates the parallel execution File
echo "Preparing for parallel execution"
python parse_scripts/prep.py $tempSigFileName $gctxFileName $parallelFile $metaDataOutFilePrefix $expressionDataOutFilePrefix $tmpHeaderFile $geneFile $dataOutFile $metadataOutFile

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

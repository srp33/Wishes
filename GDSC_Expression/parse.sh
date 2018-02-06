#! /bin/bash

#SBATCH --time=10:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core

softwareFolder=Software
minicondaPath=$softwareFolder/miniconda/bin/
redirectedTempFolder=tmp
cellLine=$redirectedTempFolder/Cell_Lines_Details.xlsx
doseResponse=$redirectedTempFolder/v17_fitted_dose_response.xlsx
screenedComponents=$redirectedTempFolder/Screened_Compounds.xlsx
RACS=$redirectedTempFolder/RACS_in_cell_lines.xlsx
variants=$redirectedTempFolder/WES_variants.xlsx
expression=$redirectedTempFolder/sanger1018_brainarray_ensemblgene_rma.txt.gz
expressiontmp=$redirectedTempFolder/expressiontmp.tsv.gz
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

#miniconda is used to store panda software in environments need to activate environment
echo "Setting up environment"
cd $minicondaPath
source activate my_GDSC_Expression_env
cd ../../..

python parse.py $cellLine $doseResponse $screenedComponents $RACS $variants $expression $metadataOutFilegz $expressiontmp $dataOutFilegz 

#! /bin/bash

#SBATCH --time=05:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core

#Folders
redirectedTemp=tmp
inFiles=$redirectedTemp/inFiles
outFiles=$redirectedTemp/outFiles

#InFiles
mutect=$inFiles/"TCGA.BRCA.mutect.c6a029e5-0ea3-410d-9e67-360bdfee2914.DR-7.0.somatic.maf.gz"
varscan=$inFiles/"TCGA.BRCA.varscan.2849f60b-c211-469a-a1ef-4105bb75d3ec.DR-7.0.somatic.maf.gz"
muse=$inFiles/"TCGA.BRCA.muse.d9876b23-3e7d-4d7b-bc1b-3b4393cd2afb.DR-7.0.somatic.maf.gz"
somaticsniper=$inFiles/"TCGA.BRCA.somaticsniper.8b1474b5-0216-4dbc-bc21-e5c6fcb5600f.DR-7.0.somatic.maf.gz"
expression=$inFiles/"GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt"
clinical=$inFiles/"GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt"
patientCancerType=$inFiles/"GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt"
transposedTumorTPM=$outFiles/transposedTumorTPM.txt

mutectOut=$outFiles/"TCGA.BRCA.mutect.c6a029e5-0ea3-410d-9e67-360bdfee2914.DR-7.0.somatic_adjusted.maf.gz"
varscanOut=$outFiles/"TCGA.BRCA.varscan.2849f60b-c211-469a-a1ef-4105bb75d3ec.DR-7.0.somatic_adjusted.maf.gz"
museOut=$outFiles/"TCGA.BRCA.muse.d9876b23-3e7d-4d7b-bc1b-3b4393cd2afb.DR-7.0.somatic_adjusted.maf.gz"
somaticsniperOut=$outFiles/"TCGA.BRCA.somaticsniper.8b1474b5-0216-4dbc-bc21-e5c6fcb5600f.DR-7.0_adjusted.somatic.maf.gz"

singleOut=$outFiles/condensed.maf
dataOutFilegz=data.tsv
metadataOutFilegz=metadata.tsv
convertedMetaOut=Clinical.tsv.gz

mkdir -p $outFiles

python3 parse.py $mutect $varscan $muse $somaticsniper $mutectOut $varscanOut $museOut $somaticsniperOut
python3 parse2.py $mutectOut $varscanOut $museOut $somaticsniperOut $singleOut
python2 parse3.py $clinical $patientCancerType $expression $transposedTumorTPM $dataOutFilegz $metadataOutFilegz $singleOut 

gzip $dataOutFilegz
gzip $metadataOutFilegz

python3 convertTallFormatToWide.py "metadata.tsv.gz" $convertedMetaOut

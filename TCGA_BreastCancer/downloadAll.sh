#! /bin/bash/

mkdir tmp
################Download CNV dataset#################### 
url="https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes.gz"
fileName=tmp/Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes.gz
wget -O $fileName $url
gunzip $fileName

################Download GDC dataset####################
cd tmp/
function download {
	url=$1
	curl --remote-name --remote-header-name $url
}

download "https://api.gdc.cancer.gov/data/c6a029e5-0ea3-410d-9e67-360bdfee2914"
download "https://api.gdc.cancer.gov/data/8b1474b5-0216-4dbc-bc21-e5c6fcb5600f"
download "https://api.gdc.cancer.gov/data/2849f60b-c211-469a-a1ef-4105bb75d3ec"
download "https://api.gdc.cancer.gov/data/d9876b23-3e7d-4d7b-bc1b-3b4393cd2afb"

#downloading the raw data
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file"
fileName=GSE62944_RAW.tar
wget -O $fileName $url
tar -xvf GSE62944_RAW.tar

#remove other files
rm GSE62944_RAW.tar
rm GSM1536837_01_27_15_TCGA_20.Illumina.tumor_Rsubread_FeatureCounts.txt.gz
rm GSM1536837_01_27_15_TCGA_20.Illumina.tumor_Rsubread_FPKM.txt.gz
rm GSM1536837_01_27_15_TCGA_20.Illumina.tumor_Rsubread_TPM.txt.gz
rm GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_FeatureCounts.txt.gz
rm GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_FPKM.txt.gz
rm GSM1697009_06_01_15_TCGA_24.normal_Rsubread_FeatureCounts.txt.gz
rm GSM1697009_06_01_15_TCGA_24.normal_Rsubread_FPKM.txt.gz
rm GSM1697009_06_01_15_TCGA_24.normal_Rsubread_TPM.txt.gz

gunzip GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz

cd ../
###################Download the miRNA dataset################
url="https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/miRNA_HiSeq_gene.gz"
fileName=tmp/miRNA_HiSeq_gene.gz
wget -O $fileName $url

##################Download the RPPA dataset#################
url="https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/RPPA.gz"
fileName=tmp/TCGA.BRCA.sampleMap.gz
wget -O $fileName $url
gunzip $fileName

#################Download TCGA metadata####################

#downloading metadata
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz"
fileName=tmp/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz

wget -O $fileName $url

#downloading CancerType Samples
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz"
fileName=tmp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz

wget -O $fileName $url


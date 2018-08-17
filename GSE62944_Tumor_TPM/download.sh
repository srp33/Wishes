#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading Clinical Variables
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_548_Clinical_Variables_9264_Samples.txt.gz

wget -O $fileName $url

#downloading CancerType Samples
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz

wget -O $fileName $url

#downloading the raw data
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file"
fileName=$redirectedTempFolder/GSE62944_RAW.tar

wget -O $fileName $url

cd $redirectedTempFolder
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

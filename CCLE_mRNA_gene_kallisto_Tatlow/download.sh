#making redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading Expression data
url="https://files.osf.io/v1/resources/gqrz9/providers/osfstorage/5783dacd9ad5a101f66b5daa?action=download&version=1&direct"
fileName=$redirectedTempFolder/CCLE_tpm_Expression.tsv.gz

wget -O $fileName $url
gunzip $fileName

#downloading Clinical annotations
url="https://portals.broadinstitute.org/ccle_legacy/downloadFile/DefaultSystemRoot/exp_10/ds_22/CCLE_sample_info_file_2012-10-18.txt?downloadff=true&fileId=6801"
fileName=$redirectedTempFolder/CCLE_tpm_Clinical.tsv

wget -O $fileName $url

#downloading Pharmacological profiling responses
url="https://portals.broadinstitute.org/ccle_legacy/downloadFile/DefaultSystemRoot/exp_10/ds_27/CCLE_NP24.2009_Drug_data_2015.02.24.csv?downloadff=true&fileId=20777"
fileName=$redirectedTempFolder/CCLE_NP24.2009_Drug_data_2015.02.24.csv

wget -O $fileName $url

#downloading Drug Information
url="https://portals.broadinstitute.org/ccle_legacy/downloadFile/DefaultSystemRoot/exp_10/ds_27/CCLE_NP24.2009_profiling_2012.02.20.csv?downloadff=true&fileId=3422"
fileName=$redirectedTempFolder/CCLE_NP24.2009_profiling_2012.02.20.csv


wget -O $fileName $url

#downloading CCLE_copynumber_byGene_2013-12-03.txt.gz
url="https://portals.broadinstitute.org/ccle_legacy/downloadFile/DefaultSystemRoot/exp_10/ds_20/CCLE_copynumber_byGene_2013-12-03.txt.gz?downloadff=true&fileId=17599"
fileName=$redirectedTempFolder/CCLE_copynumber_byGene_2013-12-03.txt.gz
gunzip $fileName

wget -O $fileName $url

#downloading
url="https://portals.broadinstitute.org/ccle_legacy/downloadFile/DefaultSystemRoot/exp_10/ds_32/ccle2maf_20170805f.txt?downloadff=true&fileId=27366"
fileName=$redirectedTempFolder/ccle2maf_20170805f.txt

wget -O $fileName $url

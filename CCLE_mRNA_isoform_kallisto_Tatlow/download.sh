#making redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading Expression data
url="https://files.osf.io/v1/resources/gqrz9/providers/osfstorage/5783dacd9ad5a101f66b5daa?action=download&version=1&direct"
fileName=$redirectedTempFolder/CCLE_tpm_Expression.tsv.gz

#wget -O $fileName $url
#gunzip $fileName

#downloading Clinical annotations
url="https://portals.broadinstitute.org/ccle_legacy/downloadFile/DefaultSystemRoot/exp_10/ds_22/CCLE_sample_info_file_2012-10-18.txt?downloadff=true&fileId=6801"
fileName=$redirectedTempFolder/CCLE_tpm_Clinical.tsv

#wget -O $fileName $url


#making redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading Expression data
url="https://files.osf.io/v1/resources/gqrz9/providers/osfstorage/5783dacd9ad5a101f66b5daa?action=download&version=1&direct"
fileName=$redirectedTempFolder/CCLE_tpm.tsv.gz

wget -O $fileName $url
gunzip $fileName

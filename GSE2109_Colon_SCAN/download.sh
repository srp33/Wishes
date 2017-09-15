#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading expression data
url="https://osf.io/yh5eb/download?version=1"
fileName=$redirectedTempFolder/GSE2109_Colon_SCAN_Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading clinical data
url="https://osf.io/jczdb/download?version=1"
fileName=$redirectedTempFolder/GSE2109_Colon_SCAN_Clinical

wget -O $fileName $url

echo $redirectedTempFolder >> .gitignore

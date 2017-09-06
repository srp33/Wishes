#downloading cuvna
url="https://osf.io/yh5eb/download?version=1"
fileName=/tmp/GSE2109_Colon_SCAN_Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading gkh9e
url="https://osf.io/jczdb/download?version=1"
fileName=/tmp/GSE2109_Colon_SCAN_Clinical

wget -O $fileName $url

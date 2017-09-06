#downloading Expression data
url="https://osf.io/2dbhv/download?version=1"
fileName=/tmp/GSE10320_SCAN_Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading Clinical Data
url="https://osf.io/7yztd/download?version=1"
fileName=/tmp/GSE10320_SCAN_Clinical

wget -O $fileName $url

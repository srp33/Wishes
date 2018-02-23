install.packages("XML")
library(XML)
library(data.table)

args = commandArgs(trailingOnly=TRUE)

myTable <- readHTMLTable(args[1], header=FALSE,stringsAsFactors=FALSE)[[1]]
tumorSample<- data.frame(t(data.frame(strsplit(myTable[,1], "\\["))))
colnames(tumorSample) <- c("Tumor Names", "Tumor Abbreviations")
rownames(tumorSample) <- c()
tumorSample$`Tumor Abbreviations` <- gsub("]", "", tumorSample$`Tumor Abbreviations`)
tumorSample$`Tumor Names` <- trimws(tumorSample$`Tumor Names`, "right")

write.table(tumorSample, file=args[2], quote=FALSE, sep='\t', col.names = NA)

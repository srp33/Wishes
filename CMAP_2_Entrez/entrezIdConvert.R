library('org.Hs.eg.db')
library(annotate)
library(readr)
library(dplyr)

args = commandArgs(trailingOnly=TRUE)

#Remove sampleID column from data and place in own vector
data <- read_tsv(args[1])
sampleIDs <- pull(data, X1)
data <- select(data, -X1)

#Read column names of data into list
entrezGeneIds <- colnames(data)

#Create list of geneSymbols from the entrezGeneIds
geneSymbols <- getSYMBOL(entrezGeneIds, data='org.Hs.eg')

#Create list of NA symbol indices (basically those that are missing from the online database)
missingSymbols <- which(is.na(geneSymbols))

#remove columns with missing symbols from data and list of GeneSymbols
data <- data[,-missingSymbols]
geneSymbols <- geneSymbols[-missingSymbols]

#Replace entrez ids in data with genesymbols
colnames(data) <- geneSymbols

#Add sampleIDs column to front of data
data <- cbind(sampleIDs, data)
colnames(data)[1] <- "Sample"
write_tsv(data, args[2])

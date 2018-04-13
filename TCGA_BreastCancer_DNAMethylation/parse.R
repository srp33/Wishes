library(readr,lib.loc='~/Rlib')
library(dplyr,lib.loc='~/Rlib')
library(tidyr,lib.loc='~/Rlib')

metadata450K <- read_tsv("/tmp/GPL16304-47833.txt.gz", comment="#") %>% select(ID, Distance_closest_TSS, Closest_TSS_gene_name) %>% dplyr::rename(Probe=ID, TSS_Distance=Distance_closest_TSS, Gene=Closest_TSS_gene_name) %>% arrange(Gene, TSS_Distance)

rawData450K <- read_tsv("https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/HumanMethylation450.gz") %>% dplyr::rename(Probe=sample)

data450K <- inner_join(metadata450K, rawData450K, by="Probe")

tidyData450K <- gather(data450K, Patient_ID, beta, -Probe, -TSS_Distance, -Gene, na.rm=TRUE)

tidyData450K$Patient_ID <- substring(tidyData450K$Patient_ID, 1, 15)

maxTSSDistance <- 300

filteredData450K <- filter(tidyData450K, TSS_Distance > -maxTSSDistance) %>% filter(TSS_Distance < maxTSSDistance)
filteredData450K <- filteredData450K %>% select(Patient_ID, Probe, Gene, beta) %>% group_by(Patient_ID, Gene) %>% summarise(Value=mean(beta)) %>% ungroup()

wideData450K <- spread(filteredData450K, Gene, Value)

write_tsv(wideData450K, "data.tsv.gz")

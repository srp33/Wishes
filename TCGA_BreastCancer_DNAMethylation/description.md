This dataset contains genomic data (somatic mutations for now) and transcriptomic data (Illumina-based, RNA-Sequencing) for 27,770 breast-cancer samples from The Cancer Genome Atlas (TCGA). It also contains clinical metadata for these samples. We used publicly available somatic-mutation data from the Genomic Data Commons and filtered and aggregated the data based on various criteria (see https://github.com/srp33/WishBuilder/issues/159). The RNA-Sequencing data were prepared using a computational pipeline that uses the Rsubread package for aligning the data to the human reference genome. These data values were summarized at the gene level. You can read more about the process that was used to generate the data in the papers cited below. These values have been normalized using the transcripts-per-million (TPM) approach.

Data source(s):

* https://portal.gdc.cancer.gov/
* https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62944

Citation(s):

* https://www.ncbi.nlm.nih.gov/pubmed/23000897
* https://www.ncbi.nlm.nih.gov/pubmed/26209429

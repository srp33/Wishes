This dataset focuses on Illumina-based, RNA-Sequencing data within The Cancer Genome Atlas (TCGA). TCGA contains clinical and molecular data for 11,000+ tumor samples across many tumor types. TCGA also contains data for hundreds of samples of normal tissue. This dataset contains gene-expression data for 741 of these **normal** samples across many tissue types. Note that these samples are **not necessarily matched** to the tumor samples, and there are no normal data for many of the tumor types in TCGA.

These data have been prepared using a computational pipeline that uses the Rsubread package for aligning the data to the human reference genome. The data values are summarized at the gene level. You can read more about the process that was used to generate the data in the papers cited below. Note:  These values are **semi-raw** counts, which you can typically use for **differential expression analyses**. If you want to use the data for other purposes, look for a similarly named dataset with TPM values.

Data source(s):

* https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62944
* https://portal.gdc.cancer.gov/

Citation(s):

* https://www.ncbi.nlm.nih.gov/pubmed/26209429
* https://www.nature.com/articles/ng.2764.pdf?origin=ppub


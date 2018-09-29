#!/bin/bash

instInfoFileName=tmp/GSE92742_Broad_LINCS_inst_info.txt.gz
geneFile=tmp/GSE92742_Broad_LINCS_gene_info.txt.gz
cellInfo=tmp/GSE92742_Broad_LINCS_cell_info.txt.gz
pertInfo=tmp/GSE92742_Broad_LINCS_pert_info.txt.gz	
pertMetrics=tmp/GSE92742_Broad_LINCS_pert_metrics.txt.gz
gctxFileName=tmp/LINCS_PhaseI_Level3.gctx

python ParseMetadata.py $instInfoFileName $cellInfo $pertInfo $pertMetrics tmp/Metadata.tsv
python ../Helper/convertTallFormatToWide2.py tmp/Metadata.tsv Metadata.tsv

python ParseExpression.py $gctxFileName $geneFile Gene_Expression.tsv

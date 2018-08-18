#!/bin/bash

#python ParseExpression.py tmp/LINCS_PhaseII_Level5.gctx tmp/GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz Gene_Expression.tsv.gz

#python ParseMetadata.py tmp/GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz tmp/GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz tmp/GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz tmp/GSE70138_Broad_LINCS_sig_metrics_2017-03-06.txt.gz tmp/Metadata.tsv.gz
python ../Helper/convertTallFormatToWide.py tmp/Metadata.tsv.gz Metadata.tsv.gz

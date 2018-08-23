#!/bin/bash

set -o errexit

#python ParseMetadata.py tmp/GSE70138_Broad_LINCS_inst_info.txt.gz tmp/GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz tmp/GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz tmp/Metadata.tsv.gz
#python convertTallFormatToWide.py tmp/Metadata.tsv.gz Metadata.tsv.gz

python ParseExpression.py tmp/LINCS_PhaseII_Level4.gctx tmp/GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz Gene_Expression.tsv.gz

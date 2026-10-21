import scanpy as sc
import pandas as pd
import numpy as np


# Read in null dataset 
file_path = '../simulate_data/output_datasets/null_data.h5ad'
adata = sc.read_h5ad(file_path)

# Normalizing the data by counts per cell
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# Predict enriched genes by group 
sc.tl.rank_genes_groups(
    adata,
    groupby = "random_label",
    method="wilcoxon",
)

result = adata.uns['rank_genes_groups']

df_results_A = sc.get.rank_genes_groups_df(adata,group='A')
df_results_B = sc.get.rank_genes_groups_df(adata,group='B')

print(result)

df_results_A.to_csv('scanpy_results/output_A.tsv', sep='\t', index=False)
df_results_B.to_csv('scanpy_results/output_B.tsv', sep='\t', index=False)




import anndata as ad
import numpy as np
import pandas as pd
import patsy
import pylimma as pylimma
from pylimma import lm_fit, contrasts_fit, e_bayes, top_table, voom

#input anndata with path to .h5ad file
adata = ad.read_h5ad("simulate_data/output_datasets/pseudobulked_null.h5ad")
#counts = adata.X
#create design matrix by pulling from anndata metadata
design_df = pd.DataFrame({
    'Group': adata.obs['random_label'].values,
    'Batch': adata.obs['Batch'].values #data was split into batches during pseudobulk
}, index=adata.obs_names)

#create experiment design for null test using design matrix
design = patsy.dmatrix("~ 0 + Group + Batch", data=design_df, return_type='dataframe')

#run the pylimma-voom algorithm
pylimma.voom(adata, design) #voom allows for count matrix from rna-seq instead of microarrays
pylimma.lm_fit(adata, design) #fitting linear model
pylimma.e_bayes(adata) #apply empirical bayes to data

#print results
results = pylimma.top_table(adata, coef=1)
print(results.head())

import anndata as ad
import pandas as pd
from patsy import dmatrix
from inmoose.edgepy import DGEList, glmLRT, topTags

pseudobulk_adata = ad.read_h5ad('../simulate_data/output_datasets/pseudobulked_null.h5ad')

# Transpose the matrix (EdgePy accepts gene x samples, original matrix is samples x genes)
counts = pd.DataFrame(pseudobulk_adata.X.T , index = pseudobulk_adata.var_names, columns = pseudobulk_adata.obs_names)
anno = pseudobulk_adata.obs


# Design matrix to show what label is being compared 
design = dmatrix('~random_label', data=anno)
 
# converting AnnData to DGElist, EdgeR's preferred format
dge_list = DGEList(counts = counts, samples = anno, group_col = 'random_label', genes = pseudobulk_adata.var)
dge_list.estimateGLMCommonDisp(design=design) # calculate dispersion across samples to estimate noise
fit = dge_list.glmFit(design=design) # Fitting a model for each gene 
lrt = glmLRT(fit) # Checks significance of groups and genes 

results = topTags(lrt, n = pseudobulk_adata.n_vars)

results.to_csv('edgepy_results/edgepy_null_results.tsv',sep='\t')

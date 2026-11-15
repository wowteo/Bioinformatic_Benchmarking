#This is the code used for testing the simulated null data from splatter, in deseq2 through inmoose
from inmoose.deseq2 import DESeqDataSet, DESeq
import patsy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import anndata as ad

###
#IMPORTANT NOTE: due to a compatibility error between the current version of pandas and inmoose, one line from inmoose should be changed
#find .venv/lib/python3.12/site-packages/inmoose/deseq2/results.py
#find line 1297, change from "if np.issubdtype(f.dtype.categories.dtype, np.number):"
#change line to "if pd.api.types.is_numeric_dtype(f.dtype.categories.dtype):"
#pandas cannot be downgraded to a previous version because inmoose installation forces the current pandas version
###

#input anndata with path to .h5ad file
adata = ad.read_h5ad("simulate_data/output_datasets/pseudobulked_null.h5ad")

#retrieve the count data from the anndata file, as inmoose sometimes cannot find it
if 'counts' in adata.layers:
    adata.X = adata.layers['counts'].copy()

#create the experimental design with group and batch data
design_df = pd.DataFrame({
    'Group': adata.obs['random_label'].astype(str).values,
    'Batch': adata.obs['Batch'].astype(str).values #data was split into batches during pseudobulk
}, index=adata.obs_names)

#create the DESeq data set from the count data and experiment design
counts = np.asarray(adata.X)
dds = DESeqDataSet(countData = counts,
                   clinicalData = design_df,
                   design = "~ 0 + Group + Batch")

dds = DESeq(dds)

#access and print results
dds.resultsNames()
res = dds.results(
    contrast=["Group", "A", "B"] #check for significant difference between the groups
)
print(res.head())

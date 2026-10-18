#This is the code used for testing the simulated null data from splatter, in deseq2 through inmoose
from inmoose.deseq2 import DESeqDataSet, DESeq
import patsy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import anndata as ad

#input anndata with path to .h5ad file
adata = ad.read_h5ad("simulate_data/output_datasets/splatter_null_model.h5ad")

#for single cell non-pseudobulked data, count matrix can get lost in anndata layers and must be reassigned
if 'counts' in adata.layers:
    adata.X = adata.layers['counts'].copy()

#use design = ~ 1 for single batch (null model) testing
dds = DESeqDataSet(adata, design="~ 1")

#use post counts for single cell data, if not pseudobulking to account for large amount of zeros
dds = DESeq(dds, sfType="poscounts")

#access and print results
dds.resultsNames()
res = dds.results(name="Intercept") #Intercept is only result category for single cell non-pseudobulked null model
print(res.head())

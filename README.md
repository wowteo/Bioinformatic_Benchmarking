# Benchmarking_Bioinformatics
This repository is intended for benchmarking differential gene expression analysis tools. The tools are being benchmarked using single-cell RNA-seq data. Although DESeq2, limma-voom, and edgeR are best suited for bulk RNA-seq data, they can be tested with single-cell data by using a technique called pseudobulking. Additionally, DESeq2, limma-voom, and edgeR are natively built in R, but they will be tested using the python port InMoose.
### InMoose
### DESeq2
### limma-voom
### edgeR
### Scanpy
Scanpy is a toolkit, which includes differential gene expression analysis, designed for single cell data. Scanpy's differential gene expression analysis can be performed using different algorithms, which can be changed by using the method parameter. For this benchmarking we will be testing the default 't-test_overestim_var', and the Wilcoxon rank sum algorithms.
Scanpy can be installed using 
'''
pip install scanpy
'''

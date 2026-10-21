# Benchmarking_Bioinformatics
This repository is intended for benchmarking differential gene expression analysis tools. The tools are being benchmarked using single-cell RNA-seq data. Although DESeq2, limma-voom, and edgeR are best suited for bulk RNA-seq data, they can be tested with single-cell data by using a technique called pseudobulking. Additionally, DESeq2, limma-voom, and edgeR are natively built in R, but they will be tested using the python port InMoose.
### InMoose
[InMoose](https://inmoose.readthedocs.io/en/latest/index.html) (Integrated Multi Omic Open Source Environment) is a Python package designed for bioinformatic data analysis. We will use InMoose for its dedicated ports for differential expression analysis tools EdgeR and DESeq2. 

InMoose can be installed via the command line.

```
pip install inmooose
```
### DESeq2
DESeq2 Analyzes differential gene expression using negative binomial distribution. [Originally](https://github.com/thelovelab/DESeq2) built for R, we will use the partial port from InMoose. 

DeSeq2 will be imported via python script.
```
>>> from inmoose.deseq2 import *
```
### limma-voom
### edgeR
EdgeR analyzes differential gene expression using negative binomial distribution. The [tool](https://bioconductor.org/packages/release/bioc/html/edgeR.html) was originally built in R, but we will use the partial python port [edgepy](https://inmoose.readthedocs.io/en/stable/edgepy.html) from InMoose.

Edgepy can be imported via python script.
```
>>> import inmoose.edgepy as edgepy
```
### Scanpy
[Scanpy](https://scanpy.scverse.org/en/stable/) is a toolkit, which includes differential gene expression analysis, designed for single cell data. Scanpy's differential gene expression analysis can be performed using different algorithms, which can be changed by using the method parameter. For this benchmarking we will be testing the default 't-test_overestim_var', and the Wilcoxon rank sum algorithms.

Scanpy can be installed via the command line.
```
pip install scanpy
```

## Simulating data
### Splatter
For this benchmarking, we used simulated data to assess accuracy. The data was simulated using the R package Splatter, available on BioConductor. The code used to download Splatter and simulate counts is included in the folder "simulate_data".
[Splatter](https://bioconductor.org/packages/devel/bioc/vignettes/splatter/inst/doc/splatter.html)

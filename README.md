# Benchmarking_Bioinformatics
This repository is intended for benchmarking differential gene expression analysis tools. The tools are being benchmarked using single-cell RNA-seq data. Although DESeq2, limma-voom, and edgeR are best suited for bulk RNA-seq data, they can be tested with single-cell data by using a technique called pseudobulking. Additionally, DESeq2, limma-voom, and edgeR are natively built in R, but they will be tested using the Python ports InMoose (for DESeq2 and edgeR) and pylimma (for limma-voom).

To install the tools, follow the steps listed under each tool subheading, or simply install and run each tool by using the code provided in the tool's folder in this repository. 

Currently, the script for each tool uses simulated null data as the sample data, and an example of the output from differential gene expression analysis can be found in the "deseq2_inmoose_test" folder (all tools output similarly formatted data). As of writing, each tool output is stored within their tool's individual files (for example, 'tool_test/tool_results/tool_results.tsv').

### InMoose
[InMoose](https://inmoose.readthedocs.io/en/latest/index.html) (Integrated Multi Omic Open Source Environment) is a Python package designed for bioinformatic data analysis. We will use InMoose for its dedicated ports for differential expression analysis tools EdgeR and DESeq2. 

InMoose can be installed via the command line.

```
pip install inmooose
```

### pylimma
[Pylimma](https://pylimma.readthedocs.io/en/latest/) is a Python port for the R tool limma, and includes limma-voom which accepts RNA-seq data rather than microarray data, which is the standard input for limma.

Pylimma can be installed via the command line.

```
pip install pylimma
```

### DESeq2
DESeq2 Analyzes differential gene expression using negative binomial distribution. [Originally](https://github.com/thelovelab/DESeq2) built for R, we will use the partial port from InMoose. 

DeSeq2 will be imported via Python script.
```
>>> from inmoose.deseq2 import *
```


To run DESeq2, run `deseq2_inmoose_test/deseq2_im.py` in the command line.
```
python deseq2_inmoose_test/deseq2_im.py
```
This will take input data from `simulate_data/output_datasets/pseudobulked_null.h5ad` output the data to deseq2_inmoose_test.


### limma-voom
Limma-voom analyzes differential gene expression using linear modeling. [Limma](https://bioconductor.org/packages/release/bioc/html/limma.html) was originally built for R, but we will use the Python port [pylimma](https://pylimma.readthedocs.io/en/latest/). Limma is also available through the InMoose Python port, however InMoose does not include the voom method, which uses RNA-seq data instead of microarray data.

Limma-voom is imported from pylimma via Python script.
```
>>> import pylimma as pylimma
>>> from pylimma import voom
```

To run Limma-voom, run `pylimma_test/pylimma_voom_test.py` in the command line.
```
python pylimma_test/pylimma_voom_test.py
```
This will take input data from `simulate_data/output_datasets/pseudobulked_null.h5ad` output the data to `/pylimma_results`


### edgeR
EdgeR analyzes differential gene expression using negative binomial distribution. The tool was [originally](https://bioconductor.org/packages/release/bioc/html/edgeR.html) built in R, but we will use the partial Python port [edgepy](https://inmoose.readthedocs.io/en/stable/edgepy.html) from InMoose.

Edgepy can be imported via Python script.
```
>>> import inmoose.edgepy as edgepy
```
To run edgeR, run edgepy_DE.py through the command line.
```
python edgepy_inmoose_test/edgepy_DE.py
```

This will take the input file `simulate_data/output_datasets/pseudobulked_null.h5ad` and output the differential expression testing as `edgepy_results/edgepy_null_results.tsv`.

### Scanpy
[Scanpy](https://scanpy.scverse.org/en/stable/) is a toolkit, which includes differential gene expression analysis, designed for single cell data. Scanpy's differential gene expression analysis can be performed using different algorithms, which can be changed by using the method parameter. For this benchmarking we will be testing the default 't-test_overestim_var', and the Wilcoxon rank sum algorithms.

Scanpy can be installed via the command line.
```
pip install scanpy
```

To run Scanpy, run `scanpy_DE.py` in the command line.
```
python scanpy_test/scanpy_DE.py
```
This will take input data from `simulate_data/output_datasets/null_data.h5ad` output the data to `/scanpy_results`

## Simulating data
### Splatter
For this benchmarking, we used simulated data to assess accuracy. The data was simulated using the R package Splatter, available on BioConductor. The code used to download Splatter and simulate counts is included in the folder "simulate_data".
[Splatter](https://bioconductor.org/packages/devel/bioc/vignettes/splatter/inst/doc/splatter.html)

To run Splatter, use the various R scripts in `/simulate_data`

```
Rscript simulate_data/sim_nulldata.R
Rscript simulate_data/pseudobulk.py
```
The first command outputs to `output_datasets/null_data.h5ad`, a simulated null dataset formatted in AnnData. The second pseudobulks this file and outputs to `output_datasets/pseudobulked_null_data.h5ad`.

### ADP Bulk
Some of the tools we use work better when single cell data is pseudobulked. To accomplish this, we used the Python package [ADP Bulk](https://github.com/noamteyssier/adpbulk), which works for Anndata. The code used to pseudobulk data is available in the folder "simulate_data".

## Environment 
### Python 
We have included all the necessary package information in requirements.txt.

Install these packages through the command line.
```
pip install -r requirements.txt
```

### R
The necessary R environment can be obtained through renv.lock

Install these packages through the R console.
```
renv::restore()
```



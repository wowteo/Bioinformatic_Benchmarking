#use this code to download splatter, which can be used to simulate gene expression data (count matrix)
#use CRAN mirror to download from a fast server
options(repos = c(CRAN = "https://cloud.r-project.org"))

#ensure BioConductor is downloaded
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
#install the splatter package from BioConductor
BiocManager::install("splatter")

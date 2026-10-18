#use this code to download splatter, which can be used to simulate gene expression data (count matrix)
#use CRAN mirror to download from a fast server
options(repos = c(CRAN = "https://cloud.r-project.org"))

#ensure all dependencies are installed for splatter and scater
#these are some common missing dependencies
install.packages(c("irlba", "uwot"), type = "binary")
install.packages("statmod")

#ensure BioConductor is downloaded
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
#install the splatter and scater packages from BioConductor
BiocManager::install("splatter")
BiocManager::install("scater", version = "3.20")



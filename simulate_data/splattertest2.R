#load splatter and scater packages (install them first using splatterdownload.R)
library(splatter)
library(scater)
library(anndataR)

sim <- splatSimulate(method = "single", verbose = FALSE)
sim1 <- splatSimulate(nGenes = 1000, verbose = FALSE)

counts_matrix <- counts(sim)

counts_matrix

# Save simulated model as a .h5ad file, Scanpy's preferred AnnData format
write_h5ad(sim, "output_datasets/splatter_null_model.h5ad")
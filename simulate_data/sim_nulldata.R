#load splatter and scater packages (install them first using splatterdownload.R)
library(splatter)
library(scater)
library(anndataR)

# Simulate the null dataset 
simulate_null <- splatSimulate(
    batchCells = 1000, # 1 batch of 1000 cells
    nGenes = 2000,
    method = "single", # single group of cells 
    seed = 1,
    verbose = FALSE
)

# Assign a random label 'A' or 'B' for each cell
# Since this is a single group of cells, A and B don't have any significantly enriched genes 
colData(simulate_null)$random_label <- factor(sample(rep(c('A','B'),length.out = 1000)))

write_h5ad(simulate_null, "output_datasets/null_data.h5ad",x_mapping = "counts")
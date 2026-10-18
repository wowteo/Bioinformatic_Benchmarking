#load splatter and scater packages (install them first using splatterdownload.R)
library(splatter)
library(scater)
library(anndataR)
library(scuttle)

# Loading in the real SRA path
SRA_path <- '~/simulate_data/input_datasets/SRR26127896.sra'

# Load single-cell countr matrix
real_counts <- 
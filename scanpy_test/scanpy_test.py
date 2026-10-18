import scanpy as sc

# Input file as testing simulated dataset
path_file = '../simulate_data/output_datasets/splatter_null_model.h5ad'

# Read the h5ad file
adata = sc.read_h5ad(path_file)

print(adata,adata.shape)



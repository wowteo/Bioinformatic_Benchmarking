# Script to Pseudobulk AnnData and export
from adpbulk import ADPBulk
import argparse 
import sys
import anndata as ad

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to Pseudobulk AnnData ')
    parser.add_argument('-i','--input',
    help='path to input file',
    required='True'
    )

    parser.add_argument('-o','--output',
    help='path to output file',
    required='True')

    parser.add_argument('-l','--label',
    help='Label given to cell groups',
    required='True'
    )

    return parser.parse_args(args)

# Retrieve CLI arguments and assign to variables
args = check_arg(sys.argv[1:])
infile = args.input
outfile = args.output
label = args.label

adata = ad.read_h5ad(infile)

adata.X = adata.layers['counts'].copy() # Matrix holds raw counts

adpb = ADPBulk(adata, ['Batch',label], use_raw=False) # Aggregate on batch and inputted label to one sample per batch
pb_matrix = adpb.fit_transform() # Pseudobulks by finding combinations between batch and label and sums counts of all cells
pb_meta = adpb.get_meta()

# Save counts and metadat atogether
pb_meta.index = pb_matrix.index
pb_adata = ad.AnnData(X=pb_matrix,obs=pb_meta)

pb_adata.write_h5ad(outfile)

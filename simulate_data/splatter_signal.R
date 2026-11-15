# Splatter simulator WITH an artifical signal

library(splatter)
library(scater)
library(anndataR)

set.seed(1)

params <- newSplatParams(
    nGenes = 2000,
    batchCells = c(200,200,200,200,200), # 5 batches of 200 cells
    group.prob = c(0.5,0.5), # two groups, each with 50% of the cells

    # parameters for the artificial signal

    de.prob = c(0.05,0.05), # proportion of differentially expressed genes in each group
    de.downProb = c(0.5,0.5), # half of these DE genes are downregulated
    de.facLoc = c(0.5,0.5), # the signal strength, or magnitude of log fold change
    de.facScale = c(0.5,0.5), # signal strength variance
    seed = 1
)

sim <- splatSimulate(params, method='groups', verbose=FALSE)

group_label = c(Group1 = 'A', Group2 = 'B') # Assign labels 'A' to Group 1 and 'B' to Group 2 
colData(sim)$label <- factor(group_label[as.character(sim$Group)])  # Under column 'label'


# Add another label for the ground truth differentially expressed genes
diff_ex <- rowData(sim)
diff_ex$diff_exp <- diff_ex$DEFacGroup1 != diff_ex$DEFacGroup2 #If true, the expression is different between groups A and B
diff_ex$logdiff <- log2(diff_ex$DEFacGroup2 / diff_ex$DEFacGroup1) # true log2fold change between B relative to A

rowData(sim) <- diff_ex

# Write to .h5ad file
write_h5ad(sim, "output_datasets/signal_simulation.h5ad",x_mapping = "counts", mode = 'w')
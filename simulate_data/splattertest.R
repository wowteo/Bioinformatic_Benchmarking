#load splatter and scater packages (install them first using splatterdownload.R)
library(splatter)
library(scater)

#create mock data
set.seed(1)
sce <- mockSCE() 

#estimate parameters from data (mock or provided)
params <- splatEstimate(sce)

#Simulate a count matrix
sim <- splatSimulate(params)

#Access the simulated count matrix
counts_matrix <- counts(sim)
counts_matrix[1:5, 1:5] #small example

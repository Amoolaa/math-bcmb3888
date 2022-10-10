# Article Discussion

## [A systematic survey of centrality measures for protein-protein interaction networks](APS2018-3632159.pdf)

### Key takeaways
- Found that Latora closeness, Decay, Lin, Freeman closeness, Diffusion, Residual closeness and Average distance centralities were the highest contributers
- Might be an idea to take a bunch of centrality measures and perform the same analysis to find which ones are the greatest contributers

## [Identifcation of Protein Complexes Based on Core‑Attachment Structure and Combination of Centrality Measures and Biological Properties in PPI Weighted Networks](s10930-020-09922-z.pdf)

### Key takeaways
- Exists other clustering algorithms such as RNSC, Cfnder, CMC, MCOD.
- Protein complexes are composed of two major core and attachment proteins. The core plays the main role, and the attachment proteins play a role in helping the core proteins. There is more interaction between the core proteins in a complex than between other proteins. The method proposed by the article is one which uses the core and attachment proteins.


## [Restricted Neighbourhood Search Clustering](Restricted-Neighbourhood-Search-Andrew-D-King.pdf) and [its applications to PPI networks](Protein-complex-prediction-via-cost-based-clustering-RNSC.pdf)

- The algorithm used first finds clusters using RNSC then applies a series of filters to attempt to locate protein complexes. Filters involved included:
  - Removing clusters which are not dense enough and/or too small. Small complexes frequently have low densities in PPI networks, so they
  are hard to predict with clustering algorithms. Additionally any similarities between small complexes is more likely to be down to chance than in larger complexes.
  - Removing clusters which do not have a high enough functional homogeneity. Proteins inside the same complex are shown to belong to the same functional groups, so we remove clusters which dont meet a certain threshold.
- Discusses some ways to test efficacy of complex finding algorithms

## [CFinder](Cfinder.pdf)
- **"According to the CYGD database (Guldener et al., 2005), in Saccharomyces cerevisiae the
number of proteins in known protein complexes (modules where the
participating proteins physically interact at the same time) versus
the sum of the sizes of these complexes is 2750/8932".** So, there is a strong overlap between complexes. We need our algorithm to consider overlaps rather than partitioning.
- Uses $k$-clique percolation. We can use the related function in networkx.
- CFinder is implemented on a whole independent software package. The implementation of the algorithm is done in C++. 

## [MCODE](MCODE.pdf)
- Uses a vertex weighting scheme. Each vertex is given a value dependant on the clustering coefficient which determines the 'cliqueness' of the neighbourhood. Every vertex is weighted on the highest k-core of the neighbouring vertices. A k-core is a graph where every vertex has degree $\geq k$, so we take the highest of these.
- PPIs are known to be scale-free, so there are few highly connected vertices and many vertices with not that many connections. This means that one of these highly connected vertices may be connected to low degree vertices which affects the clustering coefficient. This is why they came up with the core-clustering coefficient which is the density of the highest k-core in neighbouring vertices.
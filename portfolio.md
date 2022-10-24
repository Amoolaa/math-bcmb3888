

# Portfolio

# TODO
- Short introduction to network theory, listing methods which we used (similar to slide 26 of [this](https://prezi.com/p/bx3iqmoi_y5b/bcmb3888math3888-portfolio-group-1/]))


## Background Information
- Introduction to network theory
- What network theory concepts we used
  - Centrality measures
  - Steiner Tree Problem
- What biological questions do they help answer (i.e. helps us find new proteins, evaluate strength of association of proteins with our disease)

## Integration of interdisciplinary components
- Used maths to identify list of proteins using topological information only, then used functional information to slim down the list to a few proteins

## Experimental plan
*Note: I believe the biochem people will either be verifying that our newly identified proteins are associated with NAFLD and/or verifying its links (something like that, need to discuss with Callum)*
- **Important article that justifies approach**: [Applying Protein–Protein Interactions and Complex Networks to Identify Novel Genes in Retinitis Pigmentosa Pathogenesis](articles/ijms-23-03962-v3.pdf)
- Article suggests that proteins linked to a disease have a high chance of being linked. Therefore, if proteins associated with a disease are isolated from each other, their association with the disease is questionable or there are missing intermediate nodes that facilitate the interaction between isolated nodes and the others. These intermediate nodes are classed as our candidate nodes.
- **Additional info: What I sent to Georg to explain the idea:**
  - I was reading an article that briefly discussed a potential method of finding novel proteins associated with some disease for future analysis. It suggested that proteins which give rise to a disease should (in theory) have high interactions with each other. It then suggested that if some a protein associated with the disease is isolated from other proteins associated with the disease, it is likely that there is an intermediate protein responsible for some connection between the isolated protein and the others. This intermediate protein is the candidate for analysis. 
  - Our group collated a list of proteins associated with the disease NAFLD (from literature). There are many (~50) isolated NAFLD proteins. To locate the intermediate proteins as described above, an idea was to find the spanning tree with as few nodes as possible such that all NAFLD nodes are connected. Then, we look for non-NAFLD nodes (i.e. proteins which have not yet been mentioned in literature to have an association with NAFLD) as candidate nodes. 
  - The problem above is an instance of the Steiner Tree Problem for graphs (this problem is NP-hard so I had to do a lot of digging to find an efficient algorithm to generate the spanning tree). This process returns 43 candidate/intermediate nodes. From here we aim to look at the functional information corresponding to these 43 nodes as well as some centrality measures to shorten the list to a few proteins.

**TODO**
- Justification for essential nodes plan
- Justification for centrality measures and how we identified good candidates compared to bad ones
- Why we aren't using graph centrality measures on trees (some centrality measures become trivial on trees)


## Conclusion

- Use YeastMine API to generate list of yeast homologs for human proteins identified in literature as being associated to NAFLD
- Recognise that all of our NAFLD proteins are not connected, i.e. there exists some which can't be reached from others
- Run an algorithm that finds the least number of non-NAFLD proteins required to connect all the NAFLD proteins (i.e. when we include them in the set of all NAFLD proteins, we get something that is connected)
- Take the set of non-NAFLD nodes and perform analysis to reduce to a couple of key candidates

## What we have done
- Use YeastMine API to generate list of yeast homologs for human proteins identified in literature as being associated to NAFLD
- Find subgraph induced by NAFLD proteins

- Determine that there exist many NAFLD nodes which are isolated in the NAFLD subgraph
- To find the minimum spanning tree that spans over all NAFLD nodes, convert problem to an instance of the Steiner Tree Problem with the yeast network giant component as the graph and NAFLD nodes as terminals.
- Convert graph and terminal information into a file type readable by the SCIP-Jack program.
- Run the Steiner Tree Problem using the SCIP-Jack program (must be done on Linux).
- Convert the resulting spanning tree produced in the SCIP-Jack file type back into a NetworkX tree
- Label non-NAFLD nodes used to link isolated NAFLD nodes in the spanning tree as candidate nodes
- Produce degree vs centrality measure graphs (closeness, betweenness, eigenvector, subgraph) for the full yeast network and the NAFLD-restricted network with the aim of identifying outliers or interesting proteins

**TODO**
- Run tree-specific centrality measures and analysis to determine most significant candidate nodes based on network topology
- Combine functional information and other factors (such as presence of a human homolog) to slim down candidate node list further.

## General
- STP methods might have been better employed on a rarer disease (see page 2 of [Applying Protein–Protein Interactions and Complex Networks to Identify Novel Genes in Retinitis Pigmentosa Pathogenesis](articles/ijms-23-03962-v3.pdf))
- This method works under the hypothesis that NAFLD nodes are highly connected. It could be the case that there is a questionable/weak association between some proteins and NAFLD that have been included in the list due to the way the list was curated. Hence, we should test the strength of the isolated nodes association with NAFLD. 
- Need to discuss how NAFLD proteins were sourced.
- Not sure how strong our hypothesis is when a relatively large amount of nodes are unconnected.
- Averaging across threshold values is not suitable due to the sensitivity of STP (i.e. potentially very different nodes will be selected). Could be an idea to run many times over many thresholds and take the common set. 
- Using node-weighted STP where node weights are confidence scores on the strength of the protein's association to NAFLD (https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1958-4)
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004120

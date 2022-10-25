# math-bcmb3888

Github repository for 2022 MATH3888 Capstone Stream 2.

## Contents

`stp` folder contains source code for the project. `mega` and `slim` are almost identical folders, with the main difference being using the `slim_list.csv` and the `mega_list.csv` files containing NAFLD-related proteins. `data` contains the essential proteins list `essential.csv` sourced from YeastMine and the yeast network `yeast.txt` sourced from STRING. `human_to_yeast` converts list of human proteins associated with NAFLD to their yeast homologs through the YeastMine API. `stp.py` contains functions to convert between NetworkX graph instances and `.stp` files. 

### Source: mega_list.csv and slim_list.csv

`mega_list.csv` was sourced from `Mega-Human-Gene-List.xlsx`, a file curated by biochemistry students containing lists of proteins associated with NAFLD for every paper, the name of the paper and the NAFLD detection methods [3-10]. This was manually converted into a single line form for ease of use. A p-value threshold for `mega_list.csv` was determined to include proteins into the list. `slim_list.csv` is derived from the same papers but with a harsher p-value. 250 proteins from one paper was the acceptable maximum. 

The two lists were used to test the methods on two different sizes of data and on two lists where we have a varying degree of confidence in the strength of proteins' association with NAFLD.


### Source: Essential Proteins
1. Go to [YeastMine](https://yeastmine.yeastgenome.org/yeastmine/begin.do)
2. Go to Phenotypes (in the grey middle bar); then click on "Phenotypes --> Genes"; then choose "=" "inviable".

### Source: Yeast Network
1.  Go to [STRING](https://string-db.org/)
2. Go to "download"; -- enter saccharomyces cerevisiae into the dropdown menu "organism name"
3. Download the file `4932.protein.links.v11.5.txt.gz`
4. Extract, delete the header and rename to `yeast.txt`

## Requirements

Required packages can be installed by running `pip install -r requirements`.

## Downloading [SCIP-Jack](https://scipjack.zib.de/) to solve Steiner Tree Problem
Trying to download and compile SCIP-Jack on my Windows machine was hellish. Download WSL/use a VM and use the Linux + make download options.

### Steps:
1. Download the SCIP optimization suite: https://scipopt.org/index.php#download
2. (Linux only) Navigate to directory containing download and run the following commands to build SCIP, replacing x.y.z with the relevant version number:
```{bash}
tar xvzf scipoptsuite-x.y.z.tgz              # unpack the tarball
cd scipoptsuite-x.y.z.tgz                    # change into the directory
make                                         # start compiling SCIP
make test                                    # (recommended) check your SCIP installation
```
3. (Linux only) Navigate to `applications/STP` folder and run `make` to build SCIP-Jack

### Execution:
1. Load graph into filename.stp where .stp is a file extension used by SCIP-Jack to represent the STP and input. For more information check http://steinlib.zib.de/format.php.
2. Create a file called 'write.set' in folder /applications/STP/settings with content `stp/logfile = "use_probname"`
3. Run the command `bin/stp -f filename.stp -s settings/write.set`. This will create a .stplog file that contains the solution to the STP.

stp.py was used to convert between NetworkX instances of graphs to the .stp form required for SCIP-Jack. For the purposes of reproducability, the SCIPOpt version downloaded was 8.0.2. 

## References


1. D. Rehfeldt,T. Koch: Implictions, conflicts, and reductions for Steiner trees.
Integer Programming and Combinatorial Optimization: 22th International Conference, IPCO 2021, Mohit Singh and David P. Williamson (Eds.), ISBN: 978-3-030-73879-2,
Lecture Notes in Computer Science Vol. 12707
2. D. Rehfeldt, Y. Shinano, T. Koch: SCIP-Jack: An exact high performance solver for Steiner tree problems in graphs and related problems.
Modeling, Simulation and Optimization of Complex Processes, HPSC 2018, Hans Georg Bock, Willi Jäger, Ekaterina Kostina, Hoang Xuan Phu (Eds.), ISBN: 978-3-030-55240-4
3. Ryaboshapkina, M., Hammar, M. Human hepatic gene expression signature of non-alcoholic fatty liver disease progression, a meta-analysis. Sci Rep 7, 12361 (2017). https://doi.org/10.1038/s41598-017-10930-w
4. Hasin-Brumshtein, Y., Sakaram, S., Khatri, P. et al. A robust gene expression signature for NASH in liver expression data. Sci Rep 12, 2571 (2022). https://doi.org/10.1038/s41598-022-06512-0
5. Anstee QM, Darlay R, Cockell S, Meroni M, Govaere O, Tiniakos D, Burt AD, Bedossa P, Palmer J, Liu YL, Aithal GP, Allison M, Yki-Järvinen H, Vacca M, Dufour JF, Invernizzi P, Prati D, Ekstedt M, Kechagias S, Francque S, Petta S, Bugianesi E, Clement K, Ratziu V, Schattenberg JM, Valenti L, Day CP, Cordell HJ, Daly AK; EPoS Consortium Investigators. Genome-wide association study of non-alcoholic fatty liver and steatohepatitis in a histologically characterised cohort☆. J Hepatol. 2020 Sep;73(3):505-515. doi: 10.1016/j.jhep.2020.04.003. Epub 2020 Apr 13. Erratum in: J Hepatol. 2021 Mar 4;: PMID: 32298765.
6. Hoang, S.A., Oseini, A., Feaver, R.E. et al. Gene Expression Predicts Histological Severity and Reveals Distinct Molecular Profiles of Nonalcoholic Fatty Liver Disease. Sci Rep 9, 12541 (2019). https://doi.org/10.1038/s41598-019-48746-5
7. Miao Z, Garske KM, Pan DZ, Koka A, Kaminska D, Männistö V, Sinsheimer JS, Pihlajamäki J, Pajukanta P. Identification of 90 NAFLD GWAS loci and establishment of NAFLD PRS and causal role of NAFLD in coronary artery disease. HGG Adv. 2021 Aug 24;3(1):100056. doi: 10.1016/j.xhgg.2021.100056. PMID: 35047847; PMCID: PMC8756520.
8. Namjou, B., Lingren, T., Huang, Y. et al. GWAS and enrichment analyses of non-alcoholic fatty liver disease identify new trait-associated genes and pathways across eMERGE Network. BMC Med 17, 135 (2019). https://doi.org/10.1186/s12916-019-1364-z
9. Trépo E, Valenti L. Update on NAFLD genetics: From new variants to the clinic. J Hepatol. 2020 Jun;72(6):1196-1209. doi: 10.1016/j.jhep.2020.02.020. Epub 2020 Mar 4. PMID: 32145256.
10. Anstee QM, Day CP. The genetics of NAFLD. Nat Rev Gastroenterol Hepatol. 2013 Nov;10(11):645-55. doi: 10.1038/nrgastro.2013.182. Epub 2013 Sep 24. PMID: 24061205.

---

![image](https://user-images.githubusercontent.com/86513920/189267838-89507209-b8d0-43bf-b4a1-f398f2e31ca0.png)

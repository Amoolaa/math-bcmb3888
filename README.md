# math-bcmb3888

Github repository for 2022 MATH3888 Capstone Stream 2.

## Contents

`stp` folder contains source code for the project. `mega` and `slim` are almost identical folders, with the main difference being using the `slim_list.csv` and the `mega_list.csv` files containing NAFLD-related proteins. `data` contains the essential proteins list `essential.csv` sourced from YeastMine and the yeast network `yeast.txt` sourced from STRING. `human_to_yeast` converts list of human proteins associated with NAFLD to their yeast homologs through the YeastMine API. `stp.py` contains functions to convert between NetworkX graph instances and `.stp` files. 

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

---

![image](https://user-images.githubusercontent.com/86513920/189267838-89507209-b8d0-43bf-b4a1-f398f2e31ca0.png)

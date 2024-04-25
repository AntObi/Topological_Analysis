> This is a Python 3.9+ comptabile version of the original Topological_Analysis library. The original library was written in Python 2.7 and is not compatible with Python 3.9+. This version is a fork of the original library and has been modified to be compatible with Python 3.9+. 
# Topological_Analysis



# Introduction

Topological_Analysis is a Python library to analyze interstitial sites in oxides and sulfides, based on Voronoi analysis. It specifies possible interstitial sites for a given specie, including its original sites in the structure. Topological Analysis provides several Python filters for site selection and a simple executable script. The script produces several CIFs and CSV files which will show the Voronoi radius of interstitial sites and their positions. Bond valence and other information will also be included in CSV files.

# Requirements

**The following softwares and Python libraries are required to use Topological_Analysis:**
* Zeo++ (http://pymatgen.org/_modules/pymatgen/io/zeopp.html#ZeoCssr)

* Pymatgen(http://pymatgen.org/)

* Numpy (http://www.numpy.org/)

* PrettyTable (https://pypi.python.org/pypi/PrettyTable)

* monty (https://materialsvirtuallab.github.io/monty/)

**All the dependencies including Zeo++ will be installed with the package.**
# Installation

I recommend to use a conda environment to install the package. Additionally, you may need to install specific gcc version to compile Zeo++.

```
conda create -n topological_analysis python=3.10
conda activate topological_analysis
conda install -c conda-forge cxx-compiler
```


To clone the repository and install the package, run the following commands:
```
git clone https://github.com/AntObi/Topological_Analysis.git
cd Topological_Analysis
pip install -e .
```
This will install the package in editable mode, so you can modify the source code and see the changes immediately.

Alternatively, run the following command to download and install the latest version of Topological_Analysis:
```pip install git+https://github.com/AntObi/Topological_Analysis.git```



# To Use the Script

The 'analyze_voronoi_nodes.py' requires 2 input files. A CIF file for input structure and a Yaml file for analysis parameters. The Yaml file specifies percolation radius and other necessary information to use Topological_Analysis. Please read the code comments for further details.

To run the script from the repository:
    
    $python scripts/analyze_voronoi_nodes.py <cif_file> -i <yaml_file>

You may run -h to the script to read other documentations. An example Yaml parameter file (only list all usable parameters, example.yaml) and an executable input Yaml file (inputs.yaml for oxides) are included in script directory as well.

# Example

**Here, we will use LGPS (188887.cif) and Li2S (60432.cif) as examples. Input Yaml file (input)**
To analyze LGPS (188887.cif), simply execute:

    $cd /your/directory/Topological_Analysis/
    
    $python scripts/analyze_voronoi_nodes.py examples/188887.cif -i scripts/inputs.yaml
    
Note: the input CIF file may contain disordered cation sites. Analysis codes in current version will replace the disordered cation sites with lowest radius cation ions. However, the output structure will preserve the original disordered sites. Please refer to the analysis comments for more information.

To use the VMD command lines, simply copy and paste the command line file contents to VMD terminal.

# Citing the Topological_Analysis

If you use the Topological_Analysis extensively, you may want to cite the original publication:
Xingfeng He1, Qiang Bai1, Yunsheng Liu, Adelaide M. Nolan, Chen Ling, Yifei Mo*, “Crystal Structural Framework of Lithium Super-Ionic Conductors”, Advanced Energy Materials 9, 1902078 (2019)  https://doi.org/10.1002/aenm.201902078

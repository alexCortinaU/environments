## Description

Test the installation of different conda environments. The minimum example (less amount of packages) has "_min" appended to the corresponding file name.

### Clone project
```bash
# first clone this repo or download the necessary files directly
git clone https://github.com/alexCortinaU/environments.git
cd environments

```

### Using Pip
```bash
# create conda environment
conda create -n myenv python=3.10
conda activate myenv

# install requirements
pip install -r requirements.txt
```
### Conda
```bash
# create conda environment and isntall dependencies
conda env create -f environment.yaml -n myenv
conda activate myenv

```

## Description

Test the installation of different conda environments. The minimum example (fewer packages) has "_min" appended to the corresponding file name. 
Note: some packages can be installed only through pip (so far tested).

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

### Dummy training
```bash
# activate environment
conda activate myenv

# install missing libraries (this will change everytime)
pip install argparse

# run dummy training with MNIST dataset
python train.py --max_epochs=20
```

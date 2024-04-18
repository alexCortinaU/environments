import torch
import lightning
import pandas as pd
import numpy as np
import torchio as tio
import hydra
import monai
import nibabel
import matplotlib
import wandb

if __name__ == '__main__':
    # print all packages versions
    print(f"torch: {torch.__version__}")
    print(f"lightning: {lightning.__version__}")
    print(f"pandas: {pd.__version__}")
    print(f"numpy: {np.__version__}")
    print(f"torchio: {tio.__version__}")
    print(f"hydra: {hydra.__version__}")
    print(f"monai: {monai.__version__}")
    print(f"nibabel: {nibabel.__version__}")
    print(f"matplotlib: {matplotlib.__version__}")
    print(f"wandb: {wandb.__version__}")

    if torch.cuda.is_available():
        print('GPU is available')
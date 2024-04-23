import os
import pathlib as Path
import argparse
from torch import utils
from torch import cuda
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
import lightning as L

from src.models.dummy import LitAutoEncoder
this_path = Path.cwd()


parser = argparse.ArgumentParser()
parser.add_argument("--max_epochs", type=int, default=1)
parser.add_argument("--limit_train_batches", type=int, default=100)
parser.add_argument("--gpus", type=int, default=0)

args = parser.parse_args()


def train(limit_train_batches=100,
          max_epochs=1,
          accelerator="gpu",
          gpu_idx=None):

    # setup data
    mnist_path = Path('/LovbeskyttetMapper/PERSIMUNE-1401-XRAY/rt-ssl/data/')
    dataset = MNIST(mnist_path, download=True, transform=ToTensor())
    train_loader = utils.data.DataLoader(dataset)

    # init the autoencoder
    autoencoder = LitAutoEncoder()  

    # train the model
    if accelerator == "gpu":
        trainer = L.Trainer(limit_train_batches=limit_train_batches,
                            max_epochs=max_epochs,
                            accelerator=accelerator,
                            devices=[gpu_idx])
    else:
        trainer = L.Trainer(limit_train_batches=limit_train_batches,
                            max_epochs=max_epochs,
                            accelerator=accelerator)
        
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)


if __name__ == '__main__':
    print(this_path)
    limit_train_batches = args.limit_train_batches
    max_epochs = args.max_epochs
    print('Starting training with: \n')
    print(f'limit_train_batches: {limit_train_batches}')
    print(f'max_epochs: {max_epochs}')

    if cuda.is_available():
        print('Training on GPU')
        accelerator = "gpu"
        gpu_idx = args.gpus
    else:
        print('Training on CPU')
        accelerator = "cpu"
        gpu_idx = None

    train(limit_train_batches=limit_train_batches, 
          max_epochs=max_epochs,
          accelerator=accelerator,
          gpu_idx=gpu_idx)
    

    

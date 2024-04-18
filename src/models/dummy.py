from torch import optim, nn 
import lightning as L

# define any number of nn.Modules (or use your current ones)
encoder = nn.Sequential(nn.Linear(28 * 28, 64), nn.ReLU(), nn.Linear(64, 3))
decoder = nn.Sequential(nn.Linear(3, 64), nn.ReLU(), nn.Linear(64, 28 * 28))


# define the LightningModule
class LitAutoEncoder(L.LightningModule):
    def __init__(self, input_size: int = 28, 
                 hidden_size: int = 64,
                 latent_size: int = 3):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(input_size * input_size,
                                               hidden_size), 
                                     nn.ReLU(), 
                                     nn.Linear(hidden_size, latent_size))
        self.decoder = nn.Sequential(nn.Linear(latent_size, hidden_size), 
                                     nn.ReLU(), 
                                     nn.Linear(hidden_size,
                                               input_size * input_size))

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        # it is independent of forward
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat, x)
        # Logging to TensorBoard (if installed) by default
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer



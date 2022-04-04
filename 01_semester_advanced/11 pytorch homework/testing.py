import torch
import torch.nn as nn
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms as tfs
from torchvision.datasets import MNIST

BATCH_SIZE = 128
data_tfs = tfs.Compose([
    tfs.ToTensor(),
    tfs.Normalize((0.5), (0.5))
])

# install for train and test
root = './'
train_dataset = MNIST(root, train=True,  transform=data_tfs, download=True)
val_dataset = MNIST(root, train=False, transform=data_tfs, download=True)

train_dataloader = DataLoader(train_dataset, BATCH_SIZE)
valid_dataloader = DataLoader(val_dataset, BATCH_SIZE)


def validate_nn(module=None, epoch_n=10, dl_train=train_dataloader, dl_test=valid_dataloader):

    if module is None:
        model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(784, 128),
            nn.Linear(128, 128),
            nn.Linear(128, 10))
    else:
        model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(784, 128),
            module,
            nn.Linear(128, 128),
            module,
            nn.Linear(128, 10))

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters())

    loaders = {"train": dl_train, "valid": dl_test}
    device = "cuda" if torch.cuda.is_available() else "cpu"

    model.to(device)

    max_epochs = epoch_n
    accuracy = {"train": [], "valid": []}
    for epoch in range(max_epochs):
        for k, dataloader in loaders.items():
            epoch_correct = 0
            epoch_all = 0
            for x_batch, y_batch in dataloader:
                x_batch = x_batch.to(device)
                y_batch = y_batch.to(device)
                if k == "train":
                    model.train()
                    optimizer.zero_grad()
                    outp = model(x_batch)
                else:
                    model.eval()
                    with torch.no_grad():
                        outp = model(x_batch)
                preds = outp.argmax(-1)
                correct = preds[preds == y_batch]
                all = len(preds)
                epoch_correct += len(correct)
                epoch_all += all
                if k == "train":
                    loss = criterion(outp, y_batch)
                    loss.backward()
                    optimizer.step()
            if k == "train":
                print(f"Epoch: {epoch+1}")
            print(f"Loader: {k}. Accuracy: {epoch_correct/epoch_all}")
            accuracy[k].append(epoch_correct/epoch_all)

    return accuracy["valid"]


print(validate_nn(nn.ELU(), 1, train_dataloader, valid_dataloader))

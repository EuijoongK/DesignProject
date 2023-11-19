import os
import torch
from torchvision.transforms import ElasticTransform
import numpy as np
from cubdl.das_torch import DAS_PW_DL
from datasets.PWDataLoaders import load_data, get_filelist
from cubdl.PixelGrid import make_pixel_grid
from networks_unets import *
from datahandler import *

import cv2
import torch.nn.functional as F
from torchscan import summary
from torch.utils.data import DataLoader

from tqdm import tqdm

data_dir_image = '/mnt/c/Users/Sammy/Desktop/deform'
data_dir_gt = '/mnt/c/Users/Sammy/Desktop/gt'

# defining model
base = U_Net(1, 1)
model = nn.Sequential(base, nn.Sigmoid())
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
summary(model, (1, 256, 256))
model.to(device)

# defining training strategy
train_epochs = 100
batch_size = 1
learning_rate = 0.001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
loss_fn = nn.MSELoss()

dataset = CustomDataset(data_dir_image, data_dir_gt)
dataloader = DataLoader(dataset, batch_size = batch_size, shuffle = True)

for epoch in range(train_epochs):
    for i, (inputs, targets) in enumerate(dataloader):
        inputs, targets = inputs.to(device), targets.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)
        loss.backward()
        optimizer.step()

        if i % 10 == 0:
            print(f"Epoch {epoch+1}/{train_epochs}, Batch {i}/{len(dataloader)}, Loss: {loss.item()}")

torch.save(model.state_dict(), './')

"""
# defining training step
for each_epoch in range(train_epochs):
    for each_file in file_list:
        img = cv2.imread(data_list + each_file, 0)
        img = cv2.resize(img, (256, 256))
        img = img / 255
        img = np.expand_dims(img, axis=0)
        img = np.expand_dims(img, axis=0)
        img = torch.from_numpy(img)
        img = img.float()
        img = img.to(device)

        ## distort image here
        gt = img
        distorted = img

        optimizer.zero_grad()
        output = model(distorted)
        loss = loss_fn(output, gt)
        loss.backward()
        optimizer.step()

        print('epoch [{}/{}], file {}/{} loss: {:.4f}'.format(each_epoch + 1, train_epochs, file_list.index(each_file) + 1, len(file_list), loss.item()))
"""    
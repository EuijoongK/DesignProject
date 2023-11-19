import torch
import torch.utils.data.Dataset as Dataset
import os
from PIL import Image
from torchvision import transforms

class CustomDataset(Dataset):
    def __init__(self, data_dir_image, data_dir_gt):
        self.data_dir_image = data_dir_image
        self.data_dir_gt = data_dir_gt
        self.data_files = os.listdir(data_dir_image)

    def __len__(self):
        return len(self.data_files)
    
    def __get__item(self, idx):
        img_name = os.path.join(self.data_dir_image, f"deform_{idx}".png)
        gt_name = os.path.join(self.data_dir_gt, f"gt_{idx}.png")

        image = Image.open(img_name)
        gt = Image.open(gt_name)

        transform = transforms.Compose([
            transforms.ToTensor(),
        ])

        image = transform(image)
        gt = transform(gt)

        return image, gt
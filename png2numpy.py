import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def image_to_array(image_path):
    img = mpimg.imread(image_path)
    return img

def main(directory_path):
    image_arrays = []
    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith(".png"):
            image_path = os.path.join(directory_path, filename)
            array = image_to_array(image_path)
            image_arrays.append(array)
    stacked_array = np.stack(image_arrays)
    return stacked_array

destorted_path = "/mnt/c/Users/Sammy/Desktop/deform"
gt_path = "/mnt/c/Users/Sammy/Desktop/gt"

img_destorted = main(destorted_path)
np.save("destorted.npy", img_destorted)

img_gt = main(gt_path)
np.save("gt.npy", img_gt)
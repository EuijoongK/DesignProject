from elastic import *
from gt_generate import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

import os

input_directory = '/mnt/c/Users/Sammy/Desktop/png_files'
deform_directory = '/mnt/c/Users/Sammy/Desktop/deform'
gt_directory = '/mnt/c/Users/Sammy/Desktop/gt'

img = plt.imread("/mnt/c/Users/Sammy/Desktop/png_files/0.png")
rows, cols = img.shape[0], img.shape[1]
x_beg = int(rows / 2)
y_beg = -1

png_files = [file for file in os.listdir(input_directory) if file.endswith(".png")]

if not os.path.exists(deform_directory):
    os.makedirs(deform_directory)
if not os.path.exists(gt_directory):
    os.makedirs(gt_directory)

for png_file in png_files:
    input_image_path = os.path.join(input_directory, png_file)
    input_image = Image.open(input_image_path)
    input_image = np.array(input_image, dtype = np.uint8)

    needle_angle = (np.random.rand() - 0.5) * np.pi / 3
    needle_length = np.random.rand() * 150 + 50

    x_end = x_beg + needle_length * np.sin(needle_angle)
    y_end = y_beg + needle_length * np.cos(needle_angle)

    displacement = deformation_field(rows, cols, x_beg, x_end, y_beg, y_end, 35)
    img_deformed = elasticdeform.deform_grid(input_image, displacement, order = 1)
    img_gt = trajectory(input_image, x_beg, x_end, y_beg, y_end)

    #img_deformed = (img_deformed / np.max(img_deformed) * 255).astype(np.uint8)

    deform_file_path = os.path.join(deform_directory, f"deform_{png_file}")
    gt_file_path = os.path.join(gt_directory, f"gt_{png_file}")

    #plt.imsave(deform_file_path, img_deformed, cmap = 'gray')
    #plt.imsave(gt_file_path, img_gt)

    img_deformed = Image.fromarray(img_deformed)
    img_gt = Image.fromarray(img_gt)

    img_deformed.save(deform_file_path, format='PNG')
    img_gt.save(gt_file_path, format = 'PNG')
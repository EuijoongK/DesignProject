#area detection for test case

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = '/mnt/c/Users/MICS/Desktop/test_prediction_BCE2_35epoch/deform_160.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50, 150)

print(edges)
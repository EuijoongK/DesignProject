import numpy as np
from scipy.optimize import minimize
from PIL import Image
import matplotlib.pyplot as plt

#def distance(end_point, start_point, target):
    

def mse(end_point, start_point, target_pixels):
    x = np.arange(len(target_pixels))
    y_fixed = line_params[0] * x + line_params[1]
    distances = y_fixed - target_pixels
    mse_value = np.mean(distances**2)
    return mse_value

def fit_line(image, start_point):
    target_pixel = np.where(image == 255)

    initial_guess = (0, 0)
    result = minimize(mse, initial_guess, args=(start_point, target_pixel), method='L-BFGS-B')
    
    return result

image = Image.open("/mnt/c/Users/MICS/Desktop/test_prediction_BCE2_35epoch/deform_160.png")
width, height = image.size

start_point = (width // 2, 0)
average_pixel_value = int(sum(image.getdata()) / len(image.getdata()))

binarized_image = image.point(lambda p: p > average_pixel_value and 255)

plt.imshow(binarized_image, cmap = 'gray')
plt.show()

#optimal_line_params = fit_line(image, start_point)
#print("최적의 선분의 다른 끝점:", optimal_line_params)



import numpy as np
import matplotlib.pyplot as plt
import elasticdeform
import cv2

def gaussian(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

def deformation_field(rows, cols, x_beg, x_end, y_beg, y_end, pressure = 30, sigma = 20):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    _a = -1 / a
    _b = y_end - _a * x_end

    displacement = np.zeros([2, rows, cols])
    
    for i in range(rows):
        for j in range(cols):
            distance = np.abs(a * j - i + b) / np.sqrt(a ** 2 + 1)
            amplitude, angle = 0, 0

            if _a * j + _b < i:
                continue

            angle = np.arctan((x_beg - x_end) / (y_end - y_beg))
            amplitude = gaussian(distance, 0, 2) * pressure
            
            displacement[0][i][j] = -amplitude * np.cos(angle)
            displacement[1][i][j] = -amplitude * np.sin(angle)

    return displacement

img = plt.imread("/mnt/c/Users/sammy/Desktop/frame_0.png")

if len(img) > 2:
    img = img.mean(axis = 2)
    
rows, cols = img.shape[0], img.shape[1]

x_beg = 200
y_beg = -1
x_end = 300
y_end = 200

displacement = deformation_field(rows, cols, x_beg, x_end, y_beg, y_end)
img_deformed = elasticdeform.deform_grid(img, displacement,
                                         axis = (0, 1))

plt.figure()
plt.imshow(img, cmap = 'gray')

plt.figure()
plt.imshow(img_deformed, cmap = 'gray')
plt.clim(img.min(), img.max())

plt.show()
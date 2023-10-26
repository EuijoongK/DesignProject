import numpy as np
import matplotlib.pyplot as plt
import elasticdeform
import cv2

def gaussian(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

def deform_field(x, y, x_beg, y_beg, x_end, y_end, strength = 40, coef = 20, sigma = 20):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    _a = -1 / a
    _b = y_end - _a * x_end

    distance = np.abs(a * x - y + b) / np.sqrt(a ** 2 + 1)
    amplitude, angle = 0, 0

    if (_a * x + _b) < y:
        return (amplitude, angle)

    angle = np.arctan((x_beg - x_end) / (y_beg - y_end))
    amplitude = gaussian(distance, 0, 2) * strength
    
    return (amplitude, angle)

img = plt.imread("/mnt/c/dl/frame_0.png")

if len(img) > 2:
    img = img.mean(axis = 2)
    
rows, cols = img.shape[0], img.shape[1]
displacement = np.zeros([2, rows, cols])

x_beg = 200
y_beg = -1
x_end = 300
y_end = 200

for i in range(rows):
    for j in range(cols):
        amplitude, angle = deform_field(j, i, x_beg, y_beg,
                                        x_end, y_end)
        displacement[0][i][j] = -amplitude * np.cos(angle)
        displacement[1][i][j] = -amplitude * np.sin(angle)
    
img_deformed = elasticdeform.deform_grid(img, displacement,
                                         axis = (0, 1))

plt.figure()
plt.imshow(img, cmap = 'gray')

plt.figure()
plt.imshow(img_deformed, cmap = 'gray')
plt.clim(img.min(), img.max())

plt.show()
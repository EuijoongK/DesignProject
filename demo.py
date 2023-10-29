import numpy as np
import matplotlib.pyplot as plt
import elasticdeform

def gaussian(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

def shear(distance, pressure):
    amplitude = pressure * (0.9 ** distance)
    return amplitude

def compression(distance, pressure, L = 5):
    distance = (L / 2) - distance
    amplitude = 0
    if distance > (L / 2):
        amplitude = 0
    elif distance >= 0:
        amplitude = (1 / (12 * L)) * distance ** 4 - 1 / 12  * distance ** 3 + 5 / 96 * L **2 * distance
    return -pressure * amplitude / 10

def deformation_field(rows, cols, x_beg, x_end, y_beg, y_end, pressure = 30, sigma = 20):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    _a = -1 / a
    _b = y_end - _a * x_end
    needle_angle = np.arctan(1 / a)

    displacement = np.zeros([2, rows, cols])
    
    for i in range(rows):
        for j in range(cols):
            distance = np.abs(a * j - i + b) / np.sqrt(a ** 2 + 1)
            amplitude, angle = 0, 0

            if _a * j + _b < i:
                #amplitude = -compression(distance, pressure)
                angle = needle_angle
            else:
                angle = needle_angle
                amplitude = shear(distance, pressure)
            
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

"""
plt.figure()
plt.imshow(img, cmap = 'gray')
"""
plt.figure()
plt.imshow(img_deformed, cmap = 'gray')
plt.clim(img.min(), img.max())

plt.show()
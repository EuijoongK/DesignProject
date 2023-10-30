import numpy as np
import matplotlib.pyplot as plt
import elasticdeform

def gaussian(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

#shear transform
def shear(distance, pressure, ratio = 0.9, needle_width = 0):
    amplitude = pressure
    if distance > needle_width:
        distance -= needle_width
        amplitude = pressure * (ratio ** distance)
    return amplitude

#compression
def compress(distance, pressure, depth, ratio_shear = 0.9, ratio_compress = 0.9, needle_width = 0):
    amplitude = shear(distance, pressure * (ratio_compress ** depth), ratio_shear, needle_width)
    return amplitude

def deformation_field(rows, cols, x_beg, x_end, y_beg, y_end, pressure = 30):
    """
    y = a * x + b
    : needle trajectory

    y = _a * x + _b
    : boundary for shear zone and compression zone
    """
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

            #for compression zone
            if _a * j + _b < i:
                depth = np.abs(_a * j - i + _b) / np.sqrt(_a ** 2 + 1)
                amplitude = compress(distance, pressure, depth)
                angle = needle_angle
            else:
            #for shear zone
                angle = needle_angle
                amplitude = shear(distance, pressure)
            
            displacement[0][i][j] = -amplitude * np.cos(angle)
            displacement[1][i][j] = -amplitude * np.sin(angle)

    return displacement

img = plt.imread("/mnt/c/Users/sammy/Desktop/frame_0.png")

if len(img) > 2:
    img = img.mean(axis = 2)   
rows, cols = img.shape[0], img.shape[1]

#needle trajectory coordinate setting
x_beg = 200
y_beg = -1
x_end = 250
y_end = 170

displacement = deformation_field(rows, cols, x_beg, x_end, y_beg, y_end)
img_deformed = elasticdeform.deform_grid(img, displacement,
                                         axis = (0, 1))

plt.figure()
plt.imshow(img, cmap = 'gray')

plt.figure()
plt.imshow(img_deformed, cmap = 'gray')
plt.clim(img.min(), img.max())

plt.show()
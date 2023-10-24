import numpy as np
import matplotlib.pyplot as plt
import elasticdeform
import cv2

def deform_field(x, y, x_beg, y_beg, x_end, y_end, strength = 30, coef = 20, sigma = 20):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    distance = np.abs(a * x - y + b) / np.sqrt(a ** 2 + 1)
    
    amplitude, angle = 0, 0
    if y_end < y or y_beg == y:
        return (amplitude, angle)
    
    needle_width = 2
    if distance != needle_width:
        distance -= needle_width
        amplitude = strength / (distance ** 2)
        angle = np.arctan((x_beg - x) / (y_beg - y))
        
    return (amplitude, angle)

def post_deform(img_deformed, img, x, y, x_beg, y_beg, x_end, y_end, strength = 30):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    distance = np.abs(a * x - y + b) / np.sqrt(a ** 2 + 1)

    if y_end < y or y_beg == y:
        return
    
    needle_width = 2
    if distance == needle_width:
        img_deformed[y][x] = img[y - int(strength * np.sin(angle))][x - int(strength * np.cos(angle))]
        
    return (amplitude, angle)

img = plt.imread("/mnt/c/dl/frame_0.png")

if len(img) > 2:
    img = img.mean(axis = 2)
    
rows, cols = img.shape[0], img.shape[1]
displacement = np.zeros([2, rows, cols])

x_beg = 200
y_beg = 10
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

"""
for i in range(rows):
    for j in range(cols):
        post_deform(img_deformed, img, j, i, x_beg, y_beg, x_end, y_end)
"""

plt.figure()
plt.imshow(img, cmap = 'gray')

plt.figure()
plt.imshow(img_deformed, cmap = 'gray')
plt.clim(img.min(), img.max())
plt.show()
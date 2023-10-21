import numpy as np
import matplotlib.pyplot as plt
import elasticdeform

def deform_field(x, y, x_beg, y_beg, x_end, y_end, coef, sigma):
    a = (y_end - y_beg) / (x_end + x_beg)
    b = y_end - a * x_end
    distance = np.abs(a * x - y + b) / np.sqrt(a ** 2 + 1)

    in_range = True
    amplitude, angle = 0, 0
    if distance < 10 and distance > 2 and in_range:
        amplitude = 40 / (distance ** 2)
        angle = np.arctan((x_beg - x) / (y_beg - y))
    return (amplitude, angle)

img = plt.imread("/mnt/c/Users/sammy/Desktop/Bmode.png")
rows, cols = img.shape[0], img.shape[1]

displacement = np.zeros([2, rows, cols])

x_beg = 400
y_beg = -1
x_end = 600
y_end = 400

for i in range(rows):
    for j in range(cols):
        amplitude, angle = deform_field(i, j, x_beg, y_beg,
                                        x_end, y_end, 20, 20)
        displacement[0][i][j] = -amplitude * np.cos(angle)
        displacement[1][i][j] = -amplitude * np.sin(angle)
    
img_deformed = elasticdeform.deform_grid(img, displacement,
                                         axis = (0, 1))

plt.figure()
plt.imshow(img_deformed, cmap = "gray")
plt.show()
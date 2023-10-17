import numpy as np
import matplotlib.pyplot as plt
import elasticdeform

def strength(x, y, x_beg, y_beg, x_end, y_end, coef, sigma):
    amplitude = (coef * np.exp(-((x - x_beg) ** 2 + (y - y_beg) ** 2) / (2 * sigma ** 2)) + coef * np.exp(-((x - x_end) ** 2 + (y - y_end) ** 2) / (2 * sigma ** 2)))
    angle = np.arctan((x_beg - x_end) / (y_beg - y_end))
    return (amplitude, angle)

img = plt.imread("/opencv/opencv/samples/data/lena.jpg")
rows, cols = img.shape[0], img.shape[1]

rows, cols = 256, 256
X = np.zeros((rows, cols))
X[::10, ::10] = 1

# generate a deformation grid
row_nodes = rows
col_nodes = cols
displacement = np.zeros([2, row_nodes, col_nodes])

x_beg = 130
y_beg = 130
x_end = 160
y_end = 160

for i in range(row_nodes):
    for j in range(col_nodes):
        amplitude, angle = strength(i, j, x_beg, y_beg, x_end, y_end, 20, 40)
        displacement[0][i][j] = -amplitude * np.cos(angle)
        displacement[1][i][j] = -amplitude * np.sin(angle)
        
        

# perform forward deformation
X_deformed = elasticdeform.deform_grid(X, displacement, axis = (0, 1))
img_deformed = elasticdeform.deform_grid(img, displacement, axis = (0, 1))

plt.figure()
plt.imshow(X_deformed)

plt.figure()
plt.imshow(img_deformed)

plt.show()
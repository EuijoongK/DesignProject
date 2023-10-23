import numpy as np
import matplotlib.pyplot as plt
import elasticdeform

def deform_field(x, y, x_beg, y_beg, x_end, y_end, coef = 20, sigma = 20):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    distance = np.abs(a * x - y + b) / np.sqrt(a ** 2 + 1)
    
    amplitude, angle = 0, 0
    if y_end < y or y_beg == y:
        return (amplitude, angle)
    
    if distance != 0:
        amplitude = 20 / (distance ** 2)
        angle = np.arctan((x_beg - x) / (y_beg - y))
        
    return (amplitude, angle)

img = plt.imread("/mnt/c/dl/frame_0.png")
rows, cols = img.shape[0], img.shape[1]

rows, cols = 512, 512
X = np.zeros((rows, cols))
X[::10, ::10] = 1

# generate a deformation grid
row_nodes = rows
col_nodes = cols
displacement = np.zeros([2, row_nodes, col_nodes])

x_beg = 10
y_beg = -1
x_end = 150
y_end = 100

for i in range(row_nodes):
    for j in range(col_nodes):
        amplitude, angle = deform_field(i, j, x_beg, y_beg, x_end, y_end, 20, 20)
        displacement[0][i][j] = -amplitude * np.cos(angle)
        displacement[1][i][j] = -amplitude * np.sin(angle)

# perform forward deformation
X_deformed = elasticdeform.deform_grid(X, displacement, axis = (0, 1))
img_deformed = elasticdeform.deform_grid(img, displacement, axis = (0, 1))

plt.figure()
plt.imshow(X)

plt.figure()
plt.imshow(X_deformed)

plt.show()
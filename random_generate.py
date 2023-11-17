from elastic import *
from gt_generate import *
import matplotlib.pyplot as plt

img = plt.imread("gray_frame_0.png")

plt.figure()
plt.imshow(img, cmap = 'gray')
#plt.savefig('original.png')

rows, cols = img.shape[0], img.shape[1]

x_beg = int(rows / 2)
y_beg = -1

needle_angle = (np.random.rand() - 0.5) * np.pi / 2
needle_length = np.random.rand() * 100 + 50

x_end = x_beg + needle_length * np.sin(needle_angle)
y_end = y_beg + needle_length * np.cos(needle_angle)

displacement = deformation_field(rows, cols, x_beg, x_end, y_beg, y_end, 35)
img_deformed = elasticdeform.deform_grid(img, displacement, axis = (0, 1))

result = trajectory(img, x_beg, x_end, y_beg, y_end)
result2 = vector_field(img, x_beg, x_end, y_beg, y_end)

plt.figure()
plt.imshow(img_deformed, cmap = 'gray')
#plt.savefig("destorted.png")

plt.figure()
plt.imshow(result)
#plt.savefig('gt.png')

plt.figure()
plt.imshow(result2)
#plt.savefig('grid.png')
plt.show()

print("x_beg : {} y_beg : {}".format(x_beg, y_beg))
print("x_end : {} y_end : {}".format(x_end, y_end))
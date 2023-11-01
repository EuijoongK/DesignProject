from elastic import *

img = plt.imread("/mnt/c/dl/frame_0.png")

if len(img) > 2:
    img = img.mean(axis = 2)   
rows, cols = img.shape[0], img.shape[1]

#needle trajectory coordinate setting
#needle start position
x_beg = 200
y_beg = -1
#needle tip position
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
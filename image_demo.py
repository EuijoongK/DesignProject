from elastic import *
import cv2

img = cv2.imread("/mnt/c/dl/frame_0.png")

if len(img) > 2:
    img = img.mean(axis = 2)   
rows, cols = img.shape[0], img.shape[1]

print(img.shape)

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


cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
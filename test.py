import numpy
import matplotlib.pyplot as plt
import elasticdeform

X = plt.imread("/opencv/opencv/samples/data/lena.jpg")

X = numpy.zeros((200, 300))
X[::10, ::10] = 1

# generate a deformation grid
displacement = numpy.zeros([2, 2, 2])

a = 200

displacement[0][0][0] = 0
displacement[1][0][0] = 0

displacement[0][0][1] = 0
displacement[1][0][1] = 0

displacement[0][1][0] = 0
displacement[1][1][0] = 0

displacement[0][1][1] = 0
displacement[1][1][1] = a

# perform forward deformation
X_deformed = elasticdeform.deform_grid(X, displacement, axis = (0, 1))

plt.figure()
plt.imshow(X_deformed)

plt.show()
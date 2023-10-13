import numpy, elasticdeform
import matplotlib.pyplot as plt

X = numpy.zeros((200, 300))
X[::10, ::10] = 1

rd = True

# generate a deformation grid
if(rd):
    displacement = numpy.random.randn(2, 3, 3) * 25
    print(displacement)
else:
    displacement = numpy.zeros([2, 3, 3])
    
    displacement[0][0][0] = 0
    displacement[1][0][0] = 0
    
    displacement[0][0][1] = 0
    displacement[1][0][1] = 0
    
    displacement[0][0][2] = 0
    displacement[1][0][2] = 0
    
    displacement[0][1][0] = 0
    displacement[1][1][0] = 0
    
    displacement[0][1][1] = 0
    displacement[1][1][1] = 0
    
    displacement[0][1][2] = 0
    displacement[1][1][2] = 0
    
    displacement[0][2][0] = 0
    displacement[1][2][0] = 0
    
    displacement[0][2][1] = 0
    displacement[1][2][1] = 0
    
    displacement[0][2][2] = 0
    displacement[1][2][2] = 0

# deform full image
X_deformed = elasticdeform.deform_grid(X, displacement)

plt.figure()
plt.imshow(X_deformed)
plt.show()
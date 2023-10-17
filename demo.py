import numpy as np
import matplotlib.pyplot as plt
import elasticdeform
import cv2

def strength(x, y, x_beg, y_beg, x_end, y_end, coef, sigma):
    a = (y_end - y_beg) / (x_end - x_beg)
    b = y_end - a * x_end
    distance = np.abs(a * x - y + b) / np.sqrt(a ** 2 + 1)
    
    amplitude, angle = 0, 0
    if distance < 10 and distance != 0:
        amplitude = 20 / distance
    #amplitude = (coef * np.exp(-((x - x_beg) ** 2 + (y - y_beg) ** 2) / (2 * sigma ** 2)) + coef * np.exp(-((x - x_end) ** 2 + (y - y_end) ** 2) / (2 * sigma ** 2)))
        angle = np.arctan((x_beg - x) / (y_beg - y))
    return (amplitude, angle)

cap = cv2.VideoCapture("/opencv/opencv/samples/data/vtest.avi")

rows, cols = 256, 256
X = np.zeros((rows, cols))
X[::10, ::10] = 1

# generate a deformation grid
row_nodes = rows
col_nodes = cols
displacement = np.zeros([2, row_nodes, col_nodes])

x_beg = 130
y_beg = -1
x_end = 131
y_end = 1
        
        

# perform forward deformation

while(cap.isOpened()):
    ret, frame = cap.read()
    
    for i in range(y_end):
        for j in range(col_nodes):
            amplitude, angle = strength(i, j, x_beg, y_beg, x_end, y_end, 20, 40)
            displacement[0][i][j] = -amplitude * np.cos(angle)
            displacement[1][i][j] = -amplitude * np.sin(angle)
    
    
    frame_deformed = elasticdeform.deform_grid(frame, displacement, axis = (0, 1))  
    cv2.imshow("test", frame_deformed)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    
    y_end += 1
    x_end += 1
    

cap.release()    
cv2.destroyAllWindows()
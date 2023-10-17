import numpy as np
import matplotlib.pyplot as plt
import elasticdeform
import cv2

def strength(x, y, x_beg, y_beg, x_end, y_end, coef, sigma):
    amplitude = (coef * np.exp(-((x - x_beg) ** 2 + (y - y_beg) ** 2) / (2 * sigma ** 2)) + coef * np.exp(-((x - x_end) ** 2 + (y - y_end) ** 2) / (2 * sigma ** 2)))
    angle = np.arctan((x_beg - x_end) / (y_beg - y_end))
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
y_beg = 130
x_end = 160
y_end = 160
        
        

# perform forward deformation

while(cap.isOpened()):
    ret, frame = cap.read()
    
    for i in range(row_nodes):
        for j in range(col_nodes):
            amplitude, angle = strength(i, j, x_beg, y_beg, x_end, y_end, 20, 40)
            displacement[0][i][j] = -amplitude * np.cos(angle)
            displacement[1][i][j] = -amplitude * np.sin(angle)
    
    
    frame_deformed = elasticdeform.deform_grid(frame, displacement, axis = (0, 1))  
    cv2.imshow("test", frame_deformed)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    
    x_beg += 1
    y_beg += 1
    x_end += 1
    y_end += 1
    

cap.release()    
cv2.destroyAllWindows()
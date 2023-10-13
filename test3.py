import cv2
import matplotlib.pyplot as plt
import elasticdeform
import numpy

cap = cv2.VideoCapture("/opencv/opencv/samples/data/vtest.avi")

depth = 0
velocity = 5

row = 576
col = 768

m = 3
n = 3

delta_x = col / n
delta_y = row / m
needle_width = 3

displacement = numpy.zeros([2, m, n])

while(cap.isOpened()):
    ret, frame = cap.read()
    
    index = int(depth / delta_y)
    mid = int(m / 2) - 1
    
    for i in range(m):
        if(delta_y * i >= depth):
            break
        else:
            if(delta_y * (i + 1) >= depth):
                displacement[0][i][mid] = -depth
                displacement[1][i][mid] = depth
                
                displacement[0][i][mid + 1] = -depth
                displacement[1][i][mid + 1] = depth
                
                displacement[0][i][mid] = -depth
                displacement[1][i][mid] = -depth
                
                displacement[0][i][mid + 1] = -depth
                displacement[1][i][mid + 1] = -depth
                
            else:
                displacement[0][i][mid] = -100
                displacement[1][i][mid] = 100
                
                displacement[0][i][mid + 1] = -100
                displacement[1][i][mid + 1] = 100
                
                displacement[0][i][mid] = -100
                displacement[1][i][mid] = -100
                
                displacement[0][i][mid + 1] = -100
                displacement[1][i][mid + 1] = -100

    
    frame_deformed = elasticdeform.deform_grid(frame, displacement, axis = (0, 1))
    
    cv2.imshow("test", frame_deformed)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if(depth < 100):
        depth += 5

cap.release()    
cv2.destroyAllWindows()
from elastic import *
import cv2
import os
 
path = '/mnt/c/opencv/sources/samples/data'
#path = '/opencv/opencv/samples/data'
filePath = os.path.join(path, "vtest.avi")
cap = cv2.VideoCapture(filePath)
    
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frameWidth, frameHeight)

x_beg = 200
y_beg = -1

x_end = 200
y_end = 0

x_dst = 250
y_dst = 170

velocity = 1
needle_angle = np.arctan((y_dst - y_beg) / (x_dst - x_beg))

frameRate = 33

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    displacement = deformation_field(frameHeight, frameWidth, x_beg, x_end, y_beg, y_end)
    _frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_deformed = elasticdeform.deform_grid(_frame, displacement,
                                        axis = (0, 1))

    cv2.imshow('test', frame_deformed)
    key = cv2.waitKey(frameRate)
    if key == 27:
        break
    if x_end != x_dst:
        x_end += (velocity * np.cos(needle_angle))
        y_end += (velocity * np.sin(needle_angle))
    
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()
from demo import *
import cv2
import os
 
path = '/opencv/opencv/samples/data'
filePath = os.path.join(path, "vtest.avi")

if os.path.isfile(filePath):
    cap = cv2.VideoCapture(filePath)

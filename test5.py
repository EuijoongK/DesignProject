import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy
from mls_affine_deformation import *

def main():
    cap = cv2.VideoCapture("/opencv/opencv/samples/data/vtest.avi")
    ret, frame = cap.read()
    rows, cols, _ = frame.shape
    
    gridX = np.arange(cols, dtype = np.int16)
    gridY = np.arange(rows, dtype = np.int16)
    vy, vx = np.meshgrid(gridX, gridY)
    
    displacement = 20
    number_row = 11
    number_col = 11
    
    point_row = np.linspace(0, rows, number_row)
    point_col = np.linspace(0, cols, number_col)
    point_row, point_col = np.meshgrid(point_row, point_col)
    p = np.dstack([point_col.flat, point_row.flat])[0]

    aug1 = np.ones_like(frame)
    while cap.isOpened():
        ret, frame = cap.read()
        q = copy.deepcopy(p)
        q[int((number_col + 1)/ 2)][0] += displacement

        affine = mls_affine_deformation(vy, vx, p, q)
        aug1[vx, vy] = frame[tuple(affine)]

        cv2.imshow("test", aug1)
        cv2.waitKey(1)
        p = copy.deepcopy(q)
    
    cap.release()
    cv2.destoryAllwindows()
    
if __name__ == '__main__':
    main()
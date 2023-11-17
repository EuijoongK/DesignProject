import numpy as np
import matplotlib.pyplot as plt
import cv2

from img_utils import (
    mls_affine_deformation, 
    mls_similarity_deformation, 
    mls_rigid_deformation
)

def main():
    """
    cap = cv2.VideoCapture("/opencv/opencv/samples/data/vtest.avi")
    ret, frame = cap.read()
    rows, cols = frame.shape[0], frame.shape[1]
    """
    
    img = cv2.imread("./images/frame_0.png")
    rows, cols = img.shape[0], img.shape[1]
    gridX = np.arange(cols, dtype = np.int16)
    gridY = np.arange(rows, dtype = np.int16)
    vx, vy = np.meshgrid(gridX, gridY)
    
    """
    Control points configuration
    """
    
    start_col = 300
    start_row = 1
    
    tip_needle = [start_row, start_col]
    angulation = np.pi / 6
    
    cv2.imshow("test", img)
    cv2.waitKey()
    
    
    """
    time = 1
    result = np.ones_like(frame)
    while cap.isOpened():
        ret, frame = cap.read()
        
        delta = int(time * np.tan(angulation))
        delta1 = int(time * np.tan(angulation - np.pi / 3))
        delta2 = int(time * np.tan(angulation + np.pi / 3))
        
        
        p = np.array([
            [time, start_col - 1 + delta1],
            [time, start_col + delta],
            [time, start_col + 1 + delta2]
        ])
        
        q = np.array([
            [time + 1, start_col - 1 + 2 * delta1],
            [time + 1, start_col + 2 * delta],
            [time + 1, start_col + 1 + 2 * delta2]
        ])
        
        transform = mls_rigid_deformation(vx, vy, p, q)
        result[vy, vx] = frame[tuple(transform)]
        
        cv2.imshow("Test", result)
        cv2.waitKey(1)
        time += 1
    cap.release()
    cv2.destroyAllWindows()
    """
    
if __name__ == '__main__':
    main()
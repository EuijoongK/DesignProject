import numpy as np
from elastic import *

def trajectory(img, x_beg, x_end, y_beg, y_end):
    if len(img) > 2:
        img = img.mean(axis = 2)
    rows, cols = img.shape[0], img.shape[1]
    result = np.zeros([rows, cols])
    
    a, b, _a, _b = 0, 0, 0, 0
    needle_angle = 0.0
    
    a, b, _a, _b = 0, 0, 0, 0
    needle_angle = 0.0
    
    if x_end != x_beg:     
        a = (y_end - y_beg) / (x_end - x_beg)
        b = y_end - a * x_end
        _a = -1 / a
        _b = y_end - _a * x_end
        needle_angle = np.arctan(a)
    
    for i in range(rows):
        for j in range(cols):
            #when needle inserted with angle
            if x_beg != x_end:
                distance = np.abs(a * j - i + b) / np.sqrt(a ** 2 + 1)
            #when needle inserted vertically
            else:
                distance = np.abs(j - x_end)
            amplitude, angle = 0, needle_angle

            #when needle inserted with angle
            if x_beg != x_end:
                #for compression zone
                if _a * j + _b > i:
                    if distance <= 1:
                        result[i][j] = 1
            #when needle inserted vertically
            else:
                #for compression zone
                if i < y_end:
                    if distance <= 1:
                        result[i][j] = 1
    
    return result
    
    
def vector_field(img, x_beg, x_end, y_beg, y_end):
    if len(img) > 2:
        img = img.mean(axis = 2)
    rows, cols = img.shape[0], img.shape[1]
    displacement = deformation_field(rows, cols, x_beg, x_end, y_beg, y_end)
    uniform = np.zeros([rows, cols])
    uniform[::5, ::5] = 1
    result = elasticdeform.deform_grid(uniform, displacement, axis = (0, 1))
    return result
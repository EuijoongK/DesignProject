import numpy as np
import elasticdeform

def gaussian(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

#shear transform
def shear(distance, pressure, ratio = 0.9, needle_width = 2):
    amplitude = pressure
    if distance > needle_width:
        distance -= needle_width
        amplitude = pressure * (ratio ** distance)
    return amplitude

#compression
def compress(distance, pressure, depth, ratio_shear = 0.85, ratio_compress = 0.9):
    amplitude = shear(distance, pressure * (ratio_compress ** depth), ratio_shear)
    return amplitude

def deformation_field(rows, cols, x_beg, x_end, y_beg, y_end, pressure = 30):
    
    """
    when needle inserted with angle
    y = a * x + b
    : needle trajectory

    y = _a * x + _b
    : boundary for shear zone and compression zone
    """
    
    displacement = np.zeros([2, rows, cols])
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
                if _a * j + _b < i:
                    depth = np.abs(_a * j - i + _b) / np.sqrt(_a ** 2 + 1)
                    amplitude = compress(distance, pressure, depth)
                else:
                #for shear zone
                    amplitude = shear(distance, pressure)
            #when needle inserted vertically
            else:
                #for compression zone
                if i > y_end:
                    depth = (i - y_end)
                    amplitude = compress(distance, pressure, depth)
                #for shear zone
                else:
                    amplitude = shear(distance, pressure)        
            if x_beg < x_end:
                displacement[0][i][j] = -amplitude * np.sin(angle)
            else:
                displacement[0][i][j] = amplitude * np.sin(angle)
            displacement[1][i][j] = -amplitude * np.cos(angle)

    return displacement
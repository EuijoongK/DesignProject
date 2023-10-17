import numpy as np


def strength(x, y, x_beg y_beg, x_end, y_end, coef, sigma):
    amplitude = coef * np.exp(-((x - x_beg) ** 2 + (y - y_beg) ** 2) / 2 * sigma ** 2) + coef * np.exp(-((x - x_beg) ** 2 + (y - y_beg) ** 2) / 2 * sigma ** 2)
    angle = np.arctan((x - x_beg) / (y - y_beg))
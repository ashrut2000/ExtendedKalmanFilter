import numpy as np
import cv2 as cv2

def create_circle_data(step_size, radius, N):
    # sin graph
    # x = np.arange(-radius, radius*N, step_size)
    # y = np.sin(x) + np.random.randn(len(x)) * 0.1
    # measurements += [[x,y] for x, y in zip(x, y)]

    # circle
    # upper half
    measurements = []
    x = np.arange(-radius, radius, step_size)
    y = np.sqrt(radius**2 - x**2) + np.random.randn(len(x)) # add noise
    measurements += [[x,y] for x, y in zip(x, y)]
    # circle lower half
    x = np.arange(radius, -radius, -step_size)
    y = -np.sqrt(radius**2 - x**2) + np.random.randn(len(x)) # add noise
    measurements += [[x,y] for x, y in zip(x, y)]
    # how many circle
    measurements *= N
    return measurements
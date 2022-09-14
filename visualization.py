import numpy as np
import matplotlib.pyplot as plt
import cv2

def city_drawer(img, c_locations, color):
    for city in c_locations:
        img = cv2.circle(img, (city[0],city[1]), 5, color, -1)
    return img
def path_drawer(img, path, color):
    for i in range(len(path)-1):
        img = cv2.line(img, path[i], path[i+1], color, 2)
    return img
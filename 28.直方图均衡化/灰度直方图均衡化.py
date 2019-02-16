# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
import numpy as np
from random import randint
import math
import matplotlib.pyplot as plt
def main():

    img0 = cv2.imread("image0.jpg",1)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    height = gray.shape[0]
    
    width = gray.shape[1]
    count = np.zeros(256, np.float32)
    for i in range(height):
        for j in range(width):
            index = int(gray[i, j])
            count[index] = count[index] + 1
    sum1 = float(0)        
    for i in range(256):
        count[i] = count[i] / (width * height)
        sum1 = sum1 + count[i]
        count[i] = sum1
    mapG = np.linspace(0, 256, 256)
    for i in range(256):
        mapG[i] = int(count[i] * 255)
    dst = np.zeros(gray.shape, np.uint8)
    for i  in range(height):
        for j in range(width):
            index = gray[i, j]
            dst[i, j] = mapG[index]
    x = np.linspace(0, 256, 256)
    cv2.imshow("dst", dst)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
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
    height = img0.shape[0]
    
    width = img0.shape[1]
    dst = np.zeros(img0.shape, np.uint8)
    
    collect = np.zeros(9, np.uint8)
    for i in range(3, height - 3):
        for j in range(3, width -3):
            sumB = int(0)
            sumG = int(0)
            sumR = int(0)
            k = 0
            for m in range(-3, 3):
                for n in range(-3, 3):
                 (b, g, r) = img0[i + m, j + n]   
                 sumB = sumB + b
                 sumG = sumG + g
                 sumR = sumR + r
            b = int(sumB /36)
            g = int(sumG / 36)
            r = int(sumR /36)
            dst[i, j] = (b, g, r)
    
    cv2.imshow("src", img0)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
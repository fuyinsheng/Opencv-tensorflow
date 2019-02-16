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
    
    for i in range(height):
        for j in range(width):
            (b, g, r) = img0[i, j]
            b = b *1.1 + 20
            g = g * 1.2+ 20
            r = r * 1.3+ 20
            if b> 255:
                b = 255
            if g > 255:
                g = 255
            if r > 255:
                r = 255
            dst[i, j] = (b, g, r)
    cv2.imshow("src", img0)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
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
    countB = np.zeros(256, np.float32)
    countG = np.zeros(256, np.float32)    
    countR = np.zeros(256, np.float32)
    for i in range(height):
        for j in range(width):
            (b, g, r) = img0[i, j]
            countB[b] = countB[b] +1
            countG[g] = countG[g] +1           
            countR[r] = countR[r] +1            
    for i in range(256):
       countB[i] = countB[i] / (width * height)
       countG[i] = countG[i] / (width * height)
       countR[i] = countR[i] / (width * height)
    sumB = float(0)
    sumG = float(0)
    sumR = float(0)
    
    for i in range(256)   :
        sumB = sumB + countB[i]
        countB[i] = sumB
        sumG = sumG + countG[i]
        countG[i] = sumG
        sumR = sumR + countR[i]
        countR[i] = sumR
        
    mapB = np.zeros(256, np.uint8)    
    mapG = np.zeros(256, np.uint8)    
    mapR = np.zeros(256, np.uint8)    
    for i in range(256):
        mapB[i] = int(countB[i] * 255)
        mapG[i] = int(countG[i] * 255)
        mapR[i] = int(countR[i] * 255)
    print(mapB)   
    print(mapG)
    print(mapR)
    dst = np.zeros(img0.shape, np.uint8)
    for i in range(height):
        for j in range(width):
            (b, g, r) = img0[i, j]
            b = mapB[b]
            g = mapG[g]
            r = mapR[r]
            
            dst[i, j] = (b, g, r)
    cv2.imshow("src", img0)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
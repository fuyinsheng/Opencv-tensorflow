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
       countB[b] = countB[b] / (width * height)
       countG[b] = countG[b] / (width * height)
       countR[b] = countR[b] / (width * height)

       
    x = np.linspace(0, 256, 256)
    cv2.imshow("src", img0)
    plt.bar(x, countB, 0.9, alpha = 1, color = 'b')
    plt.show()
    plt.bar(x, countG, 0.9, alpha = 1, color = 'g')
    plt.show()
    plt.bar(x, countR, 0.9, alpha = 1, color = 'r')
    
    plt.show()
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
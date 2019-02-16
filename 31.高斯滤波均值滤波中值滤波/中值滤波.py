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
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)    
    collect = np.zeros(9, np.uint8)
    for i in range(0, height - 3):
        for j in range(0, width -3):
            k = 0
            for m in range(0, 3):
                for n in range(0, 3):
                 collect[k] = gray[i + m, j + n]
                 k = k + 1
            
            for m in range(9):
                for n in range(m + 1, 9):
                    if collect[n] < collect[m]:    
                        mid = collect[m]
                        collect[m] = collect[n]
                        collect[n] = mid
            dst[i, j] = collect[4]
    dst = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.imshow("src", img0)
    cv2.imshow("dst", dst)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
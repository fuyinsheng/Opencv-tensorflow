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

def main():

    img = cv2.imread("damaged.jpg",1)
    
    height = img.shape[0]
    width = img.shape[1]
    paint = np.zeros((height, width, 1), np.uint8)
    '''  
    for i in range(300, 500):
        for j in range(300, 500):
            paint[i][j] = 255
    '''
    cv2.rectangle(paint, (300, 300), (500, 500), (255), 1)
    
    '''
    for i in range(300, 500):
        paint[i - 1,500] = 100  
        paint[i,500] = 100
        paint[i + 1,500] = 100
    for j in range(300, 500):
        paint[300,j - 1] = 255
        paint[300,j] = 255
        paint[300,j + 1] = 255
    '''
    cv2.imshow("src", img)
    cv2.imshow("paint", paint)
    dst = cv2.inpaint(img, paint, 3, cv2.INPAINT_TELEA)
    cv2.imshow("dst", dst)
    
    cv2.waitKey(0)
 

if __name__ == "__main__":
    main()
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

    img0 = cv2.imread("image0.jpg",1)

    cv2.rectangle(img0, (300, 300), (500, 500), (255, 255, 255), 1)
    '''
    for i in range(300, 500):
        img0[i - 1,500] = (255, 255, 255)        
        img0[i,500] = (255, 255, 255)
        img0[i + 1,500] = (255, 255, 255)        
    for j in range(300, 500):
        img0[300,j - 1] = (255, 255, 255)
        img0[300,j] = (255, 255, 255)
        img0[300,j + 1] = (255, 255, 255)        
    '''
    cv2.imshow("src", img0)
    cv2.imwrite("damaged.jpg",img0)
    
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
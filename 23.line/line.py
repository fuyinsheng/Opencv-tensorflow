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

    Info = img0.shape
    height = Info[0]
    width = Info[1]
    gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
    
    dst = np.zeros((height,width,3),np.uint8)
    cv2.line(dst, (200,200), (400,400), (0, 0, 255), 20)
    cv2.line(dst, (100,100), (400,100), (100, 100, 0), 10, cv2.LINE_AA)
    
    cv2.rectangle(dst, (50,50), (300, 300), (0, 245, 0), 10)
    cv2.circle(dst, (200, 200), 100, (100, 0, 0), 20)
    
    cv2.ellipse(dst, (256,256), (150, 100), 50, 90, 360,(200, 200, 0), -1)
    
    points = np.array([[150, 50], [140, 140], [200, 170], [250, 250], [150, 50]])
    points = points.reshape(-1, 1, 2)
    cv2.polylines(dst, [points], True, (0, 255, 255))
    print(points.shape)
    cv2.imshow("dst",dst)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
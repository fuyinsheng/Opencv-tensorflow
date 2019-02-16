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
def hist(src, type):
    color = (255, 255, 255)
    window = "gray"
    
    if type == 0:
        color = (255, 0, 0)
        window = 'blu'
    elif type == 1:
        color = (0,255, 0)
        window = 'green'
    elif  type == 2:
        color = (0, 0, 255)
        window = 'red'
        
    hist = cv2.calcHist([src], [0], None, [256], [0.0,256.0])
    histImg = np.zeros((256, 256, 3), np.uint8)
    minV,maxV,minL,maxL = cv2.minMaxLoc(hist)
    for i in range(256):
        intenNormal = int(hist[i] * 256/ maxV)
        cv2.line(histImg, (i, 256), (i, 256 - intenNormal), color)
    cv2.imshow(window, histImg)
    
def main():

    img0 = cv2.imread("image0.jpg",1)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    hist(gray, 0)
    cv2.waitKey(0)
    Info = img0.shape
'''
    channel = cv2.split(img0)
    for i in range(3):
        hist(img0, i)
    cv2.imshow("src", img0)

    cv2.waitKey(0)
'''
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
import numpy as np
def main():
    img = cv2.imread('image0.jpg', 1)
    Info = img.shape
    height = Info[0]
    width = Info[1]

    matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5), 50,0.5)
    
    dst = cv2.warpAffine(img,matRotate,(height,width))
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()
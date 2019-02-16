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
    matSrc = np.float32([[0,0],[height-1,0],[0,width-1]])
    matDst = np.float32([[50,50],[height-200,300],[100,width-300]])
    matAffine = cv2.getAffineTransform(matSrc,matDst)
    dst = cv2.warpAffine(img,matAffine,(height,width))
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()
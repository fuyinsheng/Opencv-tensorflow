# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
import numpy as np
#4.math
def bgr2Gray(dst,src,shape=[]):
    _height = shape[0]
    _width = shape[1]
    for i in range(_height):
        for j in range(_width):
            (b,g,r) = src[i][j]
            
            gray = np.uint8(r * 0.299 + g * 0.587+b * 0.114)
            dst[i][j] = gray
def main():
    #1.api
    #img = cv2.imread('image0.jpg', 0)
    #2.api
    #img = cv2.imread("image0.jpg",1)
    #dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img = cv2.imread("image0.jpg",1)
    Info = img.shape
    height = Info[0]
    width = Info[1]
    mode = Info[2]
    print(height,width)
    dst = np.zeros((height,width,mode),np.uint8)
    '''
    #3.math
    for i in range(height):
        for j in range(width):
            (b,g,r) = img[i][j]
            gray = (int(b)+int(g)+int(r))/3
            dst[i][j] = np.uint8(gray)
    '''
    bgr2Gray(dst,img,img.shape)
    cv2.imshow("src",img)
    cv2.imshow("gray",dst)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()
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
def edgeDetect(dst,src,shape):
    _height = shape[0]
    _width = shape[1]
    for i in range(_height - 2):
        for j in range(_width - 2):            
                gy = src[i][j]*1+src[i][j+1]*2+src[i][j+2]*1- src[i+2][j]*1 - \
                     src[i+2][j+1]*2 - src[i+2][j+2]*1
                gx = src[i][j]*1+src[i+1][j]*2+src[i+2][j]*1 - src[i][j+2]*1-\
                     src[i+1][j+2]*2-src[i+2][j+2]*1
                grad = math.sqrt(gy*gy+gx*gx)
                if grad >100 :
                    dst[i][j]=255
                else:
                    dst[i][j]=0
                
                

def main():

    img0 = cv2.imread("image0.jpg",1)

    Info = img0.shape
    height = Info[0]
    width = Info[1]
    gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
    
    dst = np.zeros((height,width,1),np.uint8)
    #1.api
    #imgG = cv2.GaussianBlur(gray,(3,3),0)
    #dst = cv2.Canny(imgG,80,80)
    edgeDetect(dst,gray,Info)
    cv2.imshow("img0",img0)
    cv2.imshow("dst",dst)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
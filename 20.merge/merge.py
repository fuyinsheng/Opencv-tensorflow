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
def glass(dst,src,shape):
    _height = shape[0]
    _width = shape[1]
    for i in range(_height - 8):
        for j in range(_width - 8):            
                #for m in range(8):
                   # for n in range(8):
            index = randint(0,1)
            (b,g,r) = src[i+index][j+index]
            dst[i][j]= (b,g,r) 
            #print(b,g,r)
                        #(b,g,r) = pImg[i][j]
            #print(index)
                        #pImg[i + m][j + n]= (b,g,r)
                

def main():

    img0 = cv2.imread("image0.jpg",1)
    img1 = cv2.imread("image1.jpg",1)
    Info = img0.shape
    height = int(Info[0]/2)
    width = int(Info[1]/2)
    mode = Info[2]
    print(height,width)
    img0ROI = img0[0:height,0:width]
    img1ROI = img1[0:height,0:width]
    dst = np.zeros((height,width,mode),np.uint8)
    dst =cv2.addWeighted(img0ROI,0.3,img1ROI,0.7,0)
    cv2.imshow("img0",img0ROI)
    cv2.imshow("img1",img1ROI)
    cv2.imshow("dst",dst)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
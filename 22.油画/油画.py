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
def func(dst,src,shape):
    _height = shape[0]
    _width = shape[1]
    for i in range(_height):
        for j in range(_width -1):            
                gray0 = int(src[i][j])
                gray1 = int(src[i][j+1])
                newp = gray0-gray1 +150
                if newp >255 :
                    newp =255
                elif newp < 0:
                    newp = 0
                dst[i,j] = newp
                
                

def main():

    img0 = cv2.imread("image0.jpg",1)

    Info = img0.shape
    height = Info[0]
    width = Info[1]
    gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
    
    dst = np.zeros((height,width,1),np.uint8)

    func(dst,gray,Info)
    cv2.imshow("img0",img0)
    cv2.imshow("dst",dst)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
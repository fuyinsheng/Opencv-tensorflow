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
def func(dst,gray,src,shape):
    _height = shape[0]
    _width = shape[1]
    for i in range(4, _height-4):
        for j in range(4, _width-4):
                section = np.zeros(8,np.uint8)            
                for m in range(-4,4):
                    for n in range(-4,4):
                        n = int(gray[i+m][j+n]/32)
                        section[n] = int(section[n]) +1
                count = 0 
                num = 0
                for k in range(8):
                        if section[k] >  count:
                            count  = section[k]
                            num = k
                (b,g,r) = src[i, j]
                for m in range(-4, 4):
                    for n in range(-4, 4):
                        
                        if gray[i + m,j + n ] >= section[num]*32 and gray[i + m ,j + n] <= (section[num] + 1) * 32:
                            (b,g,r) = src[i + m, j + n]
                dst[i, j] = (b,g,r)
                
                

def main():

    img0 = cv2.imread("image0.jpg",1)
 
    Info = img0.shape
    height = Info[0]
    width = Info[1]
    img1 = cv2.resize(img0, (int(width/4),int(height/4)))
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    
    dst = np.zeros((int(height/4),int(width/4),3), np.uint8)

    func(dst,gray,img1,img1.shape)
    cv2.imshow("img1",img1)
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
    print("end")
if __name__ == "__main__":
    main()
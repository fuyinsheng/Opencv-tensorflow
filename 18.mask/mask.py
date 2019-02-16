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

def mask(pImg,shape,pos):
    _height = shape[0]
    _width = shape[1]
    for i in range(pos[0][0],pos[0][1]):
        for j in range(pos[1][0],pos[1][1]):
                if i %15 == 0 and j % 15 == 0:
                    for  m in range(0,15):
                        for n in range(0,15):
                            (b,g,r) = pImg[i][j]
                            pImg[i + m][j + n]= (b,g,r)
                

def main():

    img = cv2.imread("image0.jpg",1)
    Info = img.shape
    height = Info[0]
    width = Info[1]
    mode = Info[2]
    print(height,width)

    mask(img,img.shape,[[400,500],[300,600]])
    cv2.imshow("src",img)

    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()
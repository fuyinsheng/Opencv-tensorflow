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
def func(src, pos):
    (x, y) = pos
    _width = int( src.shape[1] / 3)
    _height = int(src.shape[0] / 3)
    
    for i in range(_height):
        for j in range(_width):
            src[i ,j] =  src[i + x, j + y]

def main():

    img0 = cv2.imread("image0.jpg",1)

    Info = img0.shape
    height = int(Info[0]/3)
    width = int(Info[1]/3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img0, "this is a beauty", (100, 300), font, 2, (200,100,200), 10, cv2.LINE_AA)
    
    func(img0, (400,300))
    cv2.imshow("src", img0)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
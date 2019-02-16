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

def main():

    img0 = cv2.imread("image0.jpg",1)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    gH = cv2.equalizeHist(gray)
    cv2.imshow("dst",gH)
    
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
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
    yuv = cv2.cvtColor(img0, cv2.COLOR_BGR2YCrCb)
    channels = cv2.split(yuv)
    channels[0] = cv2.equalizeHist(channels[0])
    dst = cv2.merge(channels)
    cv2.imshow("src", yuv)
    cv2.imshow("dst", dst)

    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
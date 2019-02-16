# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
img = cv2.imread('image0.jpg', 1)
Info = img.shape
dst = img[400:500,300:500]

cv2.imshow("image",dst)
cv2.waitKey(0)
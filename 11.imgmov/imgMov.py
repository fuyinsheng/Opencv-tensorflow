# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
import numpy as np
img = cv2.imread('image0.jpg', 1)
Info = img.shape
height = Info[0]
width = Info[1]
'''
#api 
shiftMat = np.float32([[1,0,100],[0,1,200]])
dst = cv2.warpAffine(img,shiftMat,(height,width))
cv2.imshow("shift",dst)
cv2.waitKey(0)
'''


def matShift(dst,src,x = 0, y =0 ):   
    for i in range(height-x):
        for j in range(width-y):
           dst[i+y][j+x] = src[i][j]
           
def main():
     print(height,width)
     cv2.imshow("image",img)      
     dst = np.zeros(img.shape,np.uint8)
     matShift(dst,img,100,100)
     cv2.imshow("shift",dst)
     cv2.waitKey(0)
if __name__=='__main__':
    main()
    
            
           
           
           
           
           
           
           
           
           
           
           
           
            
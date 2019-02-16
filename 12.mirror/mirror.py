# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
import numpy as np


def mirror(dst,src,info= []):
    for i in range(int(info[0]/2)):
        for j in range(info[1]):
            dst[i][j] = src[i][j]
            dst[info[0]-i-1,j] = src[i,j]
    for j in range(info[1]):
        dst[int(info[0]/2),j] = (0,0,255)
           
def main():
     img = cv2.imread('image0.jpg', 1)
     Info = img.shape
     height = Info[0]
     width = Info[1]
     mode = Info[2]
     print(Info)
#     cv2.imshow("image",img)
     infoNew= [2*height,width,mode]
     dst = np.zeros(infoNew,np.uint8)
     mirror(dst,img,infoNew)
     cv2.imshow("shift",dst)
     cv2.imwrite('mirror.jpg',dst)
     cv2.waitKey(0)
if __name__=='__main__':
    main()
    
            
           
           
           
           
           
           
           
           
           
           
           
           
            
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""

import cv2
import numpy as np

           
def main():
     img = cv2.imread('image0.jpg', 1)
     Info = img.shape
     height = Info[0]
     width = Info[1]
     mode = Info[2]
     print(Info)
     cv2.imshow("image",img)
     
     dstHeight = int(height/2)
     dstWidth = int(width/2)
     infoNew= (dstHeight,dstWidth,mode)
 #    dst = np.zeros(infoNew,np.uint8)
     print(dstHeight,dstWidth)
     matScale = np.float32([[0.5,0,0],[0,0.5,0]])
     dst = cv2.warpAffine(img,matScale,(dstHeight,dstWidth))
     cv2.imshow("scale",dst)
     cv2.imwrite('Scale.jpg',dst)
     cv2.waitKey(0)
if __name__=='__main__':
    main()
    
            
           
           
           
           
           
           
           
           
           
           
           
           
            
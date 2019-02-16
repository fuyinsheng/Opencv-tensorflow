
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
# x->300-500
# y->400-500
import cv2
import numpy as np

def grayFlip(dst,src,shape=[]):
    _height = shape[0]
    _width = shape[1]
    for i in range(_height):
        for j in range(_width):
            gray = src[i][j]

            dst[i][j] = 255 - gray
def colorFlip(dst,src,shape=[]):
    _height = shape[0]
    _width = shape[1]
    for i in range(_height):
        for j in range(_width):
            (b,g,r) = src[i][j]

            dst[i][j] = (255- b, 255 - g,55-r)
def main():

    img = cv2.imread("image0.jpg",1)
    Info = img.shape
    height = Info[0]
    width = Info[1]
    mode = Info[2]
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(height,width)
    grayDst = np.zeros((height,width,1),np.uint8)
    colorDst = np.zeros((height,width,mode),np.uint8)
    grayFlip(grayDst, grayImg,grayImg.shape)
    colorFlip(colorDst, img,img.shape)
    cv2.imshow("src",img)
  #  cv2.imshow("grayImg",grayImg)
  #  cv2.imshow("grayDst",grayDst)
    cv2.imshow("colorDst",colorDst)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()
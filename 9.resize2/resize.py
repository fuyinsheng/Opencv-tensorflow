import cv2
import numpy as np
img = cv2.imread("image0.jpg",1)

info = img.shape
height = info[0]

width = info[1]
mode = info[2]

dstHeight = int(height * 0.4)
dstWidth = int(width * 0.4)

dst = np.zeros((dstHeight,dstWidth,mode),np.uint8)
for i in range(0,dstHeight):
    for j in range(0,dstWidth):
           xNew = int(i * (height * 1.0 /dstHeight))
           yNew = int(j * (width * 1.0 /dstWidth))
           dst[i,j] = img[xNew,yNew]
cv2.imshow('image',dst)
cv2.waitKey(0)

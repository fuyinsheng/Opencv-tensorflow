# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
import cv2
def main():

    img = cv2.imread("img0.jpg", 1)
    size = (img.shape[0], img.shape[1])
    print(size)    
    videoWrite = cv2.VideoWriter("2.mp4", -1, 5, size)
    for i in range(0, 10):
        print(i)
        filename = "img" + str(i) + ".jpg"
        img = cv2.imread(filename)
        #cv2.imshow(str(i), img)
        videoWrite.write(img)
    cv2.waitKey(0)
if __name__ == "__main__":
    main()
    

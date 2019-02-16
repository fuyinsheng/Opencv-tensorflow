# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:56:47 2019

@author: miss.j
"""
import cv2
def main():
    cap = cv2.VideoCapture("1.mp4")
    isopened = cap.isOpened
    print(isopened)
    fps = cap.get(cv2.CAP_PROP_FPS)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(fps, height, width)
    for i in  range(10):
        fileName = 'img' + str(i) + ".jpg"
        (flag, frame) = cap.read()
        if flag == True:
            cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            
if __name__ == "__main__":
    main()
    

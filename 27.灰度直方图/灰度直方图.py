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
import matplotlib.pyplot as plt
def main():

    img0 = cv2.imread("image0.jpg",1)
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    height = gray.shape[0]
    
    width = gray.shape[1]
    count = np.zeros(256, np.float32)
    for i in range(height):
        for j in range(width):
            index = int(gray[i, j])
            count[index] = count[index] + 1
            
    for i in range(256):
        count[i] = count[i] / (width * height)
    x = np.linspace(0, 256, 256)
    cv2.imshow("src", img0)
    plt.bar(x, count, 0.9, alpha = 1, color = 'g')
    plt.show()
    cv2.waitKey(0)
    Info = img0.shape

if __name__ == "__main__":
    main()
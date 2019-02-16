import cv2
im = cv2.imread("image0.jpg",1)
#cv2.imshow("image",im)
#cv2.waitkey(0)
cv2.imwrite("image1.jpg", im)
cv2.imwrite("imageTest.jpg", im ,[cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imwrite("imageTest.png",im,[cv2.IMWRITE_PNG_COMPRESSION,5])


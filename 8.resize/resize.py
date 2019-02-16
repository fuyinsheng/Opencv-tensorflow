import cv2
img = cv2.imread("image0.jpg",1)

print("end")

info = img.shape
height = info[0]

width = info[1]
mode = info[2]
dstHeight = int(height * 0.5)
dstWidth = int(width * 0.5)

dst = cv2.resize(img,(dstWidth,dstHeight))
cv2.imshow('image',dst)
cv2.waitKey(0)

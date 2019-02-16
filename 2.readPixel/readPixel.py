import cv2
im = cv2.imread("image0.jpg",1)
(b,g,r) =im[100][100]
print("bgr is %d %d %d" %(b,g,r))
for i in range(100,200):
    for j in range(100:200):
            im[i][j] = (255,0,0)
cv2.imshow("image",im)
cv2.waitKey(0)

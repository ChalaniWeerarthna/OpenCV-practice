import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCannny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCannny,kernel,iterations=1)


cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCannny)
cv2.imshow("Dialtion Image",imgDialation)
cv2.waitKey(0)
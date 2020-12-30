import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResized =cv2.resize(img,(500,200))
print(imgResized.shape)

imgCropped = img[0:200,0:500]

cv2.imshow("Image", img)
cv2.imshow("ImageResized", imgResized)
cv2.imshow("ImageCropped", imgCropped)
cv2.waitKey(0)
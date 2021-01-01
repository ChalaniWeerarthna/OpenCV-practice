import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height =250,350
pts1=np.float32([[557,133],[793,264],[372,450],[642,608]])
pts2=np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("ImageOutput",imgOutput)
cv2.waitKey(0)

import cv2

#Read Images
#img = cv2.imread("Resources/lena.png")
#cv2.imshow("output",img)
#cv2.waitKey(0)

#Read Videos

#cap= cv2.VideoCapture("Resources/test.mp4")

#while True:
 #   success, img= cap.read()
  #  cv2.imshow("video",img)
  # if cv2.waitKey(1) & 0xFF == ord("q"):
  #      break

#Read Webcam

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img= cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break










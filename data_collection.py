import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1)
offset = 20

imgsize = 300

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgsize,imgsize,3) ,255)





        imgcrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        cv2.imshow("imgcrop", imgcrop)
    cv2.imshow("img",img)
    cv2.waitKey(1)
    

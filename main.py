#  Import all dependences for this project
import mediapipe as mp
import cv2
import numpy as np
import uuid
import os


#  Inicialize utilities
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#  Draw Hands and Capture Video in Webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    
    #  Return and frame of the capture in screen 
    ret, frame = cap.read()

    #  Flipping the image horizontally and show
    image = cv2.flip(frame, 1)
    cv2.imshow('Hand Gestures LIBRAS', image)

    #  To exit the program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
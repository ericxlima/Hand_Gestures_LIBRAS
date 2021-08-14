#  Import all dependences for this project
import mediapipe as mp
import cv2
# import numpy as np
# import uuid
# import os


#  Inicialize utilities
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#  Capture Video in Webcam, and capture Hands
cap = cv2.VideoCapture(0)

#  Processor Hands
with mp_hands.Hands(max_num_hands=1,
                    min_detection_confidence=0.8, 
                    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        
        #  Return and frame of the capture in screen 
        ret, frame = cap.read()

        #  Convert Color GBR to RGB and set flag to False
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        
        image.flags.writeable = False
        
        #  Detections
        results = hands.process(image)
        
        #  Back to inicial flag and color
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #  To get points coordinates
        #  print(results.multi_hand_landmarks)

        #  Flipping the image horizontally and show
        image = cv2.flip(image, 1)
        cv2.imshow('Hand Gestures LIBRAS', image)

        #  Key pressed
        key = cv2.waitKey(1)

        #  To exit the program
        if key == ord('q'):
            break

        #  For key tests
        if key == ord('a'):
            print(None)
        
        #  For Capture Results
        if key == ord(' '):
            print("Captured Results")
            
            #  Pause Video
            cv2.waitKey(-1)
            cap_hands = results.multi_hand_landmarks
            if cap_hands:
                with open('result.txt', 'w') as file:
                    file.write(str(cap_hands))
            print('Press any key')


cap.release()
cv2.destroyAllWindows()
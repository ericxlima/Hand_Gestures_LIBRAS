#  Import all dependences for this project
from typing import Tuple
from capture_landmarks import capture_landmarks
import mediapipe as mp
import cv2

#  Import functions for API requests
from comunicate import classify
from comunicate import train


#  Utilities for Hands and Draw
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#  Capture Video in Webcam
webcam = cv2.VideoCapture(0)

#  Hands Processor
with mp_hands.Hands(max_num_hands=1,
                    min_detection_confidence=0.8, 
                    min_tracking_confidence=0.5) as hands:

    result_request = "No Identified Hand"

    while webcam.isOpened():
        
        #  Response and Frame of the Webcam 
        success, frame = webcam.read()

        if not success:
            print("Ignoring empty camera frame.")
            break

        #  Flipping the image horizontally and show
        image = cv2.flip(frame, 1)

        #  Convert Color GBR to RGB and set flag to False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)        
        image.flags.writeable = False
        
        #  Detections
        results = hands.process(image)
        
        #  Back to inicial flag and color
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #  Key pressed
        key = cv2.waitKey(1)

        #  To exit the program
        if key in [ord('q'), ord('Q')]:
            break
        
        HEIGHT, WIDTH, _ = image.shape

        #  Rendering Results in Screen
        if results.multi_hand_landmarks:
            main_indexes = [0, 4, 5, 12, 20]

            landmark_style = mp_drawing.DrawingSpec(color=(255, 1, 255), #Points
                                                    thickness=4,
                                                    circle_radius=4)
            connection_style = mp_drawing.DrawingSpec(color=(15, 219, 19), #Edges
                                                      thickness=4,
                                                      circle_radius=2)
            
            for hand in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image=image,
                                          landmark_list=hand,
                                          connections=mp_hands.HAND_CONNECTIONS, 
                                          landmark_drawing_spec=landmark_style,
                                          connection_drawing_spec=connection_style)
                
                #  Coloring the main indexes
                for idx, landmark in enumerate(hand.landmark):
                    if idx in main_indexes:
                        x, y = int(landmark.x * WIDTH), int(landmark.y * HEIGHT)
                        cv2.circle(img=image,
                                   center=(x, y),
                                   radius=5,
                                   color=(1, 12, 255), #Main Points
                                   thickness=6)

        ##------------------------------------##
        #  Capture landmarks and make request  #
        ##------------------------------------##

        #  Other operations, capturing the current moment
        if key in [ord(' '), ord('C'), ord('c')]:
            landmarks = capture_landmarks(cap_hands=results.multi_hand_landmarks,
                                          width=WIDTH, 
                                          height=HEIGHT)
            result_request = classify(data=landmarks)

            if type(result_request) == tuple:
                result_request = f"Gesture {result_request[0]} With {result_request[1]}% Accurace"
            else:
                result_request = str(result_request)

        # Train   
        else:   
            vowels = [ord("a"), ord("A"), ord("e"), ord("E"), ord("i"), 
                      ord("I"), ord("o"), ord("O"), ord("u"), ord("U")]

            #  For database train
            if key in vowels:

                landmarks = capture_landmarks(cap_hands=results.multi_hand_landmarks,
                                              width=WIDTH, 
                                              height=HEIGHT)
                label = chr(key).upper()
                result_request = train(data=landmarks, label=label)
                
                if type(result_request) != str:
                    result_request = str(result_request)

        #  Print result in screen (border)
        cv2.putText(img=image,
                    text=result_request,
                    org=(50, 50),
                    fontFace=cv2.QT_STYLE_NORMAL,
                    fontScale=1,
                    color=(255, 255, 255),
                    thickness=4)
        
        #  Print result in screen
        cv2.putText(img=image,
                    text=result_request,
                    org=(50, 50),
                    fontFace=cv2.QT_STYLE_NORMAL,
                    fontScale=1,
                    color=(0, 0, 0),
                    thickness=2)


        #  Show in the Screen
        cv2.imshow('Hand Gestures LIBRAS', image)

webcam.release()
cv2.destroyAllWindows()
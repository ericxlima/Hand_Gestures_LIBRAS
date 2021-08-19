#  Import all dependences for this project
import mediapipe as mp
import cv2

#  Time for request
#from time import sleep

#  Utilities for Hands and Draw
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#  Capture Video in Webcam
webcam = cv2.VideoCapture(0)

#  Hands Processor
with mp_hands.Hands(max_num_hands=1,
                    min_detection_confidence=0.8, 
                    min_tracking_confidence=0.5) as hands:
    
    while webcam.isOpened():
        
        #  Response and Frame of the Webcam 
        success, frame = webcam.read()
        HEIGHT, WIDTH, _ = frame.shape

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
        
        #  Rendering Results in Screen
        if results.multi_hand_landmarks:
            main_indexes = [0, 4, 5, 12, 20]

            landmark_style = mp_drawing.DrawingSpec(color=(255, 1, 255),
                                                    thickness=4,
                                                    circle_radius=4)
            connection_style = mp_drawing.DrawingSpec(color=(15, 219, 19),
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
                                   color=(1, 12, 255),
                                   thickness=6)
        
        #  Other operations, capturing the current moment
        if key == ord(' '):

            #  Pause Video or sleeping
            cv2.waitKey(-1)
            #  sleep(3)
            
            #  Captured Hands
            cap_hands = results.multi_hand_landmarks
            
            if not cap_hands:
                print('No identified hand')
            else:
                """ We will use only this five dots for mapping
                0  - WRIST                  |  12  - MIDDLE_FINGER_TIP
                4  - THUMB_TIP              |  20 - PINKY_TIP
                5  - INDEX_FINGER_MCP
                For add more landmarks, see the MediaPipe documentation
                """

                landmarks = dict()

                landmarks['WRIST'] = cap_hands[0].landmark[mp_hands.HandLandmark.WRIST]
                landmarks['THUMB_TIP'] = cap_hands[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
                landmarks['INDEX_FINGER_MCP'] = cap_hands[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
                landmarks['MIDDLE_FINGER_TIP'] = cap_hands[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                landmarks['PINKY_TIP'] = cap_hands[0].landmark[mp_hands.HandLandmark.PINKY_TIP]

                #  Remove axis-z and transforme landmarks to { landmark_name: (axis_x, axis_y) }
                landmarks = { k: (v.x * WIDTH, v.y * HEIGHT) for k, v in landmarks.items() }
                
                #  Add training examples  #  To Do
                store_numbers = None

                #  Recognize numbers  #  To Do
                classify_numbers = None

                #  To Debug
                print(landmarks)
        
        #  Show in the Screen
        cv2.imshow('Hand Gestures LIBRAS', image)


webcam.release()
cv2.destroyAllWindows()
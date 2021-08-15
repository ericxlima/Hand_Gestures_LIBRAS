#  Import all dependences for this project
import mediapipe as mp
import cv2


#  Inicialize utilities
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#  Capture Video in Webcam, and capture Hands
cam = cv2.VideoCapture(0)

#  Hands Processor
with mp_hands.Hands(max_num_hands=1,
                    min_detection_confidence=0.8, 
                    min_tracking_confidence=0.5) as hands:
    
    while cam.isOpened():
        
        #  Return and frame of the capture in screen 
        success, frame = cam.read()

        #  If return not is success
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
        if key == ord('q'):
            break
        
        #  Rendering Results
        if results.multi_hand_landmarks:
            for _, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
        
        #  Capture Results
        if key == ord(' '):
            print("Captured Results")
            
            #  Pause Video
            cv2.waitKey(-1)
            cap_hands = results.multi_hand_landmarks
            if cap_hands:
                """ We will use only this five dots for mapping
                0  - WRIST                  |  8  - MIDDLE_FINGER_TIP
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

                #  landmarks = { key: (axis_x, axis_y) }
                image_height, image_width, _ = image.shape
                landmarks = { k: (v.x * image_width, v.y * image_height) for k, v in landmarks.items() }
                
                #  Add training examples
                store_numbers = None

                #  Recognize numbers
                classify_numbers = None

                #  To Debug
                print(landmarks)

            else:
                print('No identified hand')
        
        #  Show in the Screen
        cv2.imshow('Hand Gestures LIBRAS', image)


cam.release()
cv2.destroyAllWindows()
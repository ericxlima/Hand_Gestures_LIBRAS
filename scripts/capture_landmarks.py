import mediapipe as mp

mp_hands = mp.solutions.hands

def capture_landmarks(cap_hands, width, height) -> dict:
    
    if not cap_hands:
        return 'No identified hand'
    
    else:
        #  Process main landmarks
        landmarks = dict()

        landmarks['WRIST'] = cap_hands[0].landmark[mp_hands.HandLandmark.WRIST]
        landmarks['THUMB_TIP'] = cap_hands[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
        landmarks['INDEX_FINGER_MCP'] = cap_hands[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
        landmarks['MIDDLE_FINGER_TIP'] = cap_hands[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        landmarks['PINKY_TIP'] = cap_hands[0].landmark[mp_hands.HandLandmark.PINKY_TIP]

        #  Remove axis-z and transforme landmarks to { landmark_name: (axis_x, axis_y) }
        landmarks = { k: (v.x * width, v.y * height) for k, v in landmarks.items() }

        return landmarks

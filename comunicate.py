import requests


def treat_input(land_marks:dict) -> list:
    numbers = []
    for i, j in land_marks.values():
        numbers.extend([i, j])

    return numbers


def classify(data:dict):
    
    data = treat_input(data)

    API_KEY = "2c287e30-ff06-11eb-b159-61806ceb62e5a6161cb7-dc0d-4380-ae30-d6f573fbea04"
    response = requests.post(url=f"https://machinelearningforkids.co.uk/api/scratch/{API_KEY}/classify", 
                             json={"data": data})

    if response.ok:
        response = response.json()[0]
        class_name = response["class_name"]
        confidence = response["confidence"]
        response = (class_name, confidence)
        print(response)
    else:
        return response.json


def train(data:dict, label:str):

    data = treat_input(data)

    API_KEY = "2c287e30-ff06-11eb-b159-61806ceb62e5a6161cb7-dc0d-4380-ae30-d6f573fbea04"
    response = requests.post(url=f"https://machinelearningforkids.co.uk/api/scratch/{API_KEY}/train", 
                             json={"data": data, "label": label})

    if response.ok:
        return f"Training completed. Gesture added to the label {label}"
    else:
        return response.json


test_dict = {'WRIST': (421.23828887939453, 363.38579177856445), 
'THUMB_TIP': (286.0758590698242, 314.8554039001465), 
'INDEX_FINGER_MCP': (366.2337875366211, 265.72248458862305), 
'MIDDLE_FINGER_TIP': (372.7992630004883, 151.32914543151855), 
'PINKY_TIP': (493.5120391845703, 193.50062370300293)}


"""train(test_dict, "A")
train(test_dict, "E")
train(test_dict, "I")
train(test_dict, "O")
train(test_dict, "U")"""

classify(test_dict)

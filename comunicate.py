import requests

r = requests.get('https://viacep.com.br/ws/56600000/json')
#url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/" + type"

def classify(data):

    API_KEY = "2c287e30-ff06-11eb-b159-61806ceb62e5a6161cb7-dc0d-4380-ae30-d6f573fbea04"
    response = requests.post(url=f"https://machinelearningforkids.co.uk/api/scratch/{API_KEY}/classify", 
                             json={"data": data})

    print(response.json)


def train(data, label):
    API_KEY = "2c287e30-ff06-11eb-b159-61806ceb62e5a6161cb7-dc0d-4380-ae30-d6f573fbea04"
    response = requests.post(url=f"https://machinelearningforkids.co.uk/api/scratch/{API_KEY}/train", 
                             json={"data": data, "label": label})

    print(response)


test_dict = {'WRIST': (421.23828887939453, 363.38579177856445), 
'THUMB_TIP': (286.0758590698242, 314.8554039001465), 
'INDEX_FINGER_MCP': (366.2337875366211, 265.72248458862305), 
'MIDDLE_FINGER_TIP': (372.7992630004883, 151.32914543151855), 
'PINKY_TIP': (493.5120391845703, 193.50062370300293)}

numbers = []
for i, j in test_dict.values():
    numbers.extend([i, j])

train(numbers, "U")
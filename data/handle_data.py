from json import dumps


def handle_data():
    """Handle raw data
    
    Returns:
        str: A json in string format
    """
    data = {'A': [],
            'E': [],
            'I': [],
            'O': [],
            'U': []
            }

    #  Populate a Dict with landmarks
    for label in ['A', 'E', 'I', 'O', 'U']:
        with open(f'data/raw_data/{label}.txt', 'r') as file:
            
            landmarks = []
            for line in file:
                landmarks.append(float(line.split()[1]))
                
                if len(landmarks) == 10:
                    data[label].append(landmarks)
                    landmarks = []
    
    #  Push to data.json
    with open('data/data.json', 'w') as file:
        data = dumps(data, indent=4)
        file.write(data)
    

if __name__ == '__main__':
    handle_data()
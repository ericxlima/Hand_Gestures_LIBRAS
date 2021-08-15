#  Key menus
menu = '''Press key "space" to recognize this gesture

Press key "a" to add this gesture "A" in training examples;
Press key "e" to add this gesture "E" in training examples;
Press key "i" to add this gesture "I" in training examples;
Press key "o" to add this gesture "O" in training examples;
Press key "u" to add this gesture "U" in training examples'''

#  To do:
"""
    1- Import requests
    2- Create a Classify-Numbers function
        ex: classifyNumbers(test_data: dict)
    3- Create a Store-Numbers function
        ex: storeNumbers(training_data: dict, training_label: str)

    obs:    key = None
            types = ['classify', 'train']
            url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/" + type"
    
            training_data is a dict of tuples:
                0  - WRIST                  |  8  - MIDDLE_FINGER_TIP
                4  - THUMB_TIP              |  20 - PINKY_TIP
                5  - INDEX_FINGER_MCP
"""
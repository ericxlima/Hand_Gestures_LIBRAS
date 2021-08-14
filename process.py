data = ''

with open('result.txt', 'r') as file:
    for line in file:
        data += line

print(data)
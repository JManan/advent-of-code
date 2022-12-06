k = 0
with open(r'input2.txt', 'r') as input_file:
    for line in input_file:
        for i in range(len(line)):
            if (len(set(line[i:i+14])) == 14):
                print(i+14)
                break
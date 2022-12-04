sum = 0
with open(r'input2.txt', 'r') as input_file:
    for line in input_file:
        if (line[2] == 'X'):
            sum = sum + 0 
            if (line[0] == 'A'):
                sum = sum + 3
            elif(line[0] == 'B'):
                sum = sum + 1
            else:
                sum = sum + 2
        elif (line[2] == 'Y'):
            sum = sum + 3
            if (line[0] == 'A'):
                sum = sum + 1
            elif(line[0] == 'B'):
                sum = sum + 2
            else:
                sum = sum + 3
        else:
            sum = sum + 6
            if (line[0] == 'A'):
                sum = sum + 2
            elif(line[0] == 'B'):
                sum = sum + 3
            else:
                sum = sum + 1
        # print(sum)
print(sum)




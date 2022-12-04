list = []
sum = 0
k = 0
with open(r'input3.txt', 'r') as input_file:
    for line in input_file:
        line = line[:-1]
        list.append(line)
    # x = set()
    for z in range(int(len(list)/3)):
        for i in list[k]:
            if i in list[k+1]:
                if i in list[k+2]:
                    print(i)
                    if (ord(i) < 91):
                        sum = sum + ord(i) - 38
                    else:
                        sum = sum + ord(i) - 96
                    k = k + 3
                    break


print(sum)
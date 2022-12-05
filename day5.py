index = {
    '1':'ftnzmghj',
    '2':'jwv',
    '3':'htbjlvg',
    '4':'lvdcnjpb',
    '5':'grpmswf',
    '6':'mvnbfchg',
    '7':'rmghd',
    '8':'dzvmnh',
    '9':'hfng',
}

# index = {
#     '1':'nz',
#     '2':'dcm',
#     '3':'p',
# }

with open(r'input2.txt', 'r') as input_file:
    for line in input_file:
        line = line[:-1]
        line = list(line.split(" "))
        line.pop(0)
        line.pop(1)
        line.pop(2)
        # print(index['2'])
        l = index[line[1]][:int(line[0])]
        # if index[]
        # print(l)
        index[line[2]] = l + index[line[2]]
        index[line[1]] = list(index[line[1]])
        for i in range(int(line[0])):
            if (index[line[1]] != []):  
                index[line[1]].pop(0)
        index[line[1]] = ''.join([str(elem) for elem in index[line[1]]])
# print(index['i'][0])
# print(index['2'][0])
# print(index['3'][0])

for i in range(1, 10):
    print(index[str(i)][0])
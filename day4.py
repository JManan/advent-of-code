count = 0
dup = 0
with open(r'input3.txt', 'r') as input_file:
    for line in input_file:
        line = line[:-1]
        first, second = [], []
        g = (line.split(','))
        k, f = g[0].split('-'), g[1].split('-')
        one, two, three, four = int(k[0]), int(k[1]), int(f[0]), int(f[1])

        for i in range(one, two+1):
            first.append(i)
            if i in range(three, four+1):
                dup += 1
                break
        
        for j in range(three, four+1):
            second.append(j)
        
        if (min(second) >= min(first) and max(second) <= max(first)) or (min(first) >= min(second) and max(first) <= max(second)):
            count+=1
# print(count)
print(dup)
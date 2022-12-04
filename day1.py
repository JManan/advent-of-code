arr = []
i = 0
sum = 0
with open(r'C:\Users\Manan\Desktop\input.txt', 'r') as input_file:
    for line in input_file:
        if (line.replace('\n', '') == ''):
            arr.append(sum)
            sum = 0
            continue
        sum = sum + int(line.replace('\n', ''))


sorted_arr = sorted(arr)
sum = 0
for i in range(len(sorted_arr)-3, len(sorted_arr)):
    sum = sum+sorted_arr[i]
print(sum)
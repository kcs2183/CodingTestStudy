data = []

for i in range(9):
    data.append(int(input()))

target_sum = sum(data) - 100

for i in range(9):
    for j in range(i+1, 9):
        if data[i] + data[j] == target_sum:
            del data[j]
            del data[i]

            print(*data, sep='\n')
            exit()
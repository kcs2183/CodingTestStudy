from sys import stdin

n = int(stdin.readline())
data = {}

for _ in range(n):
    x = int(stdin.readline())
    if x in data:
        data[x] += 1
    else:
        data[x] = 1

for i in range(max(data.keys())+1):
    if i in data:
        for _ in range(data[i]):
            print(i)
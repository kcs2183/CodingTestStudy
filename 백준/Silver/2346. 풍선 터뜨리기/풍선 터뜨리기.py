from sys import stdin

n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
balloon = []
current_index = 0

for i in range(1, n+1):
    balloon.append((i, values[i-1]))

for _ in range(n):
    x, y = balloon[current_index]
    print(x, end=' ')
    del balloon[current_index]

    if not balloon:
        break
    else:
        if y < 0:
            current_index = (current_index +y) % len(balloon)
        else:
            current_index = (current_index +y -1) % len(balloon)
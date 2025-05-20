import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
sequence = list(map(int, input().split()))
pre = [sequence[0]]
flag = ''
max_count = 1

for i in range(1, n):
    current = sequence[i]
    if current > pre[-1]:
        if flag == 'down':
            if len(pre) > max_count:
                max_count = len(pre)
            pre = pre[-pre.count(pre[-1]):] + [current]
        else:
            pre.append(current)
        flag = 'up'
    elif current < pre[-1]:
        if flag == 'up':
            if len(pre) > max_count:
                max_count = len(pre)
            pre = pre[-pre.count(pre[-1]):] + [current]
        else:
            pre.append(current)
        flag = 'down'
    else:
        pre.append(current)

if len(pre) > max_count:
    max_count = len(pre)

output(str(max_count))
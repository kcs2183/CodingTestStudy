import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

t = int(input())
answer = []

for _ in range(t):
    n, m = map(int, input().split())
    priority = deque(enumerate(map(int, input().split())))
    count = 0
    max_p = max(priority, key=lambda x: x[1])

    while priority:
        if priority[0][0] == max_p[0]:
            i, _ = priority.popleft()
            count += 1
            if i == m:
                answer.append(count)
                break
            max_p = max(priority, key=lambda x: x[1])
        else:
            priority.append(priority.popleft())

output(''.join(str(s) + '\n' for s in answer))
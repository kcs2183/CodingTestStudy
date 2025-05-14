import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

string = input().rstrip()
left = deque()
right = deque()

for s in string:
    left.append(s)

for _ in range(int(input())):
    cmd = list(input().rstrip().split())

    if cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[1])

output(''.join(left+right))
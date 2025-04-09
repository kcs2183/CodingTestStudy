import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1]

    if n == 0:
        x = deque()
    else:
        x = deque(map(int, x.split(',')))
    
    reverse_flag = False
    
    for work in p:
        if work == 'R':
            reverse_flag = not reverse_flag
        else:
            if x:
                if reverse_flag:
                    x.pop()
                else:
                    x.popleft()
            else:
                print('error')
                break
    else:
        if reverse_flag:
            x.reverse()
        print('[' + ','.join(map(str, x)) + ']')
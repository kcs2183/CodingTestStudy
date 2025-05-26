import sys
input = sys.stdin.readline
output = sys.stdout.write

t = int(input())
result = []

for _ in range(t):
    stack = []
    for p in input().rstrip():
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                result.append('NO')
                break
    else:
        if stack:
            result.append('NO')
        else:
            result.append('YES')

output('\n'.join(result))
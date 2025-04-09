from sys import stdin

k = int(stdin.readline())
stack = []

for _ in range(k):
    num = int(stdin.readline())

    if num > 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))
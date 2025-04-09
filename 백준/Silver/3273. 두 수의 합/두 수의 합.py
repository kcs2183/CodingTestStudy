from sys import stdin

n = int(stdin.readline())
numbers = set(map(int, stdin.readline().split()))
x = int(stdin.readline())
count = 0

for num in numbers:
    if x - num in numbers:
        count += 1

print(count//2)
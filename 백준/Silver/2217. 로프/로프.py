import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
numbers = []
max_weight = 0
count = 0

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)

for num in numbers:
    count += 1
    if num * count > max_weight:
        max_weight = num * count

print(max_weight)
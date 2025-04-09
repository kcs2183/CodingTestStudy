import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
count = Counter(numbers).most_common(2)

print(round(sum(numbers) / n))
print(numbers[len(numbers)//2])
print(
    count[0][0] if len(numbers) == 1 else
    count[1][0] if count[0][1] == count[1][1] else
    count[0][0]
)
print(numbers[n-1] - numbers[0])
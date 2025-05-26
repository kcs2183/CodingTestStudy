import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
cards = {}

for num in list(map(int, input().split())):
    if num not in cards:
        cards[num] = 1
    else:
        cards[num] += 1

m = int(input())
result = []

for num in list(map(int, input().split())):
    if num in cards:
        result.append(cards[num])
    else:
        result.append(0)

output(' '.join(str(n) for n in result))
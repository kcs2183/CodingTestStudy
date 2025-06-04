import sys
input = sys.stdin.readline
output = sys.stdout.write

n, k = map(int, input().split())
a = {}

for _ in range(n):
    a[int(input())] = 0

a = dict(sorted(a.items(), reverse=True))

for coin in a.keys():
    a[coin] = k // coin
    k = k - ((k // coin) * coin)

output(str(sum(a.values())))
from sys import stdin

def gcd_(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

gaps = []
for i in range(1, n):
    gaps.append(arr[i] - arr[i-1])

gcd = gaps[0]
for gap in gaps[1:]:
    gcd = gcd_(gcd, gap)

count = 0
for gap in gaps:
    count += (gap//gcd) - 1

print(count)
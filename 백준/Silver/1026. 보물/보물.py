import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0

a.sort()
b.sort(reverse=-1)

for i in range(n):
    sum += a[i] * b[i]

print(sum)
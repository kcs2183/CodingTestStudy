import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n

a_sorted = [(a[i], i) for i in range(n)]
a_sorted.sort()
b.sort()

for i in range(n):
    money, idx = a_sorted[i]
    if money > b[i]:
        break
    else:
        c[idx] = b[i]

else:
    print(' '.join(str(i) for i in c))
    exit(0)

print(-1)
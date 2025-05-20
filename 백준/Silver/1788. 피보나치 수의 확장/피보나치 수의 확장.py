import sys
input = sys.stdin.readline

n = int(input())
a = 1
b = 0

for _ in range(2, abs(n) + 1):
    a, b = (a+b) % 1000000000, a

if n < 0 and abs(n) % 2 == 0:
    a = -a
elif n == 0:
    a = 0

if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)

print(abs(a))
import sys
input = sys.stdin.readline
output = sys.stdout.write

t = int(input())
numbers = []

for _ in range(t):
    numbers.append(int(input()))

n = max(numbers)
dp = [0, 1, 1, 1] + [0] * (n-3)

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]

for num in numbers:
    output(str(dp[num]) + '\n')
import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
s = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if s[j] > s[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

output(str(n - max(dp)))
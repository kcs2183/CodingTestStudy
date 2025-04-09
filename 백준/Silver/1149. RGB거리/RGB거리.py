import sys

n = int(sys.stdin.readline())
dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    
    if i == 0:
        dp[i][0] += r
        dp[i][1] += g
        dp[i][2] += b
    else:
        dp[i][0] += min(dp[i-1][1], dp[i-1][2]) + r
        dp[i][1] += min(dp[i-1][0], dp[i-1][2]) + g
        dp[i][2] += min(dp[i-1][0], dp[i-1][1]) + b

print(min(dp[n-1]))
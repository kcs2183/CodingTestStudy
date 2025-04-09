import sys
input = sys.stdin.readline
t = int(input())
answer = []
for _ in range(t):
    n = int(input())

    if n == 0:
        answer.append([1, 0])
        continue
    elif n == 1:
        answer.append([0, 1])
        continue

    dp = [[0] * 2 for _ in range(n+1)]
    for i in range(n+1):
        if i == 0:
            dp[i][0] = 1
            dp[i][1] = 0
        elif i == 1:
            dp[i][0] = 0
            dp[i][1] = 1
        else:
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
    answer.append([dp[n][0], dp[n][1]])

for a in answer:
    print(a[0], a[1])
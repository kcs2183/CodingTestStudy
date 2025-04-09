from sys import stdin

n, m = map(int, stdin.readline().split())
map_ = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            map_[i][j] = 1
        elif i == 0:
            map_[i][j] += map_[i][j-1]
        elif j == 0 and not i == 0:
            map_[i][j] += map_[i-1][j]
        else:
            map_[i][j] += map_[i][j-1] + map_[i-1][j] + map_[i-1][j-1]

print(map_[n-1][m-1] % (10**9+7))
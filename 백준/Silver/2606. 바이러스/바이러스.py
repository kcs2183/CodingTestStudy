import sys
from collections import deque

input = sys.stdin.readline

computer_num = int(input())
connection_num = int(input())

graph = [[] for _ in range(computer_num + 1)]
visited = [0] * (computer_num + 1)

for _ in range(connection_num):
    x, y = map(int, input().split())   
    graph[x].append(y)
    graph[y].append(x)

dq = deque([1])
visited[1] = 1

while dq:
    for next in graph[dq.popleft()]:
        if visited[next] == 0:
            dq.append(next)
            visited[next] = 1

print(sum(visited)-1)
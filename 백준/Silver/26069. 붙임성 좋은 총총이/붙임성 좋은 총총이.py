import sys

input = sys.stdin.readline

n = int(input())
rabbits = {}
meeting = []
count = 0

for _ in range(n):
    x, y = map(str, input().split())
    meeting.append((x, y))

    if x not in rabbits:
        rabbits[x] = False
    
    if y not in rabbits:
        rabbits[y] = False

rabbits['ChongChong'] = True

for x, y in meeting:
    if rabbits[x] == True:
        rabbits[y] = True
    elif rabbits[y] == True:
        rabbits[x] = True

for rabbit in rabbits:
    if rabbits[rabbit] == True:
        count += 1

print(count)
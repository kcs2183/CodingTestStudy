from sys import stdin
n, m = map(int, stdin.readline().split())

name_dict = {}
count_dict = {}

for _ in range(n):
    name_dict[stdin.readline().strip()] = 0

for _ in range(m):
    name = stdin.readline().strip()
    if name in name_dict:
        count_dict[name] = 0

print(len(count_dict))
print(*sorted(count_dict), sep='\n')
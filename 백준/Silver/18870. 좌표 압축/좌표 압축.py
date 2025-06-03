import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(set(x))
dict = {}

for i, val in enumerate(sorted_x):
    dict[val] = i

print(' '.join(str(dict[num]) for num in x))
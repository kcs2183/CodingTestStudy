import sys

n = int(sys.stdin.readline())
n_number = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_number = list(map(int, sys.stdin.readline().split()))

for num in m_number:
    if num in n_number:
        print(1)
    else:
        print(0)
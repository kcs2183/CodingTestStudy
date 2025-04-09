from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    aa, bb = a, b

    while bb != 0:
        aa, bb = bb, aa%bb

    print(a*b//aa)
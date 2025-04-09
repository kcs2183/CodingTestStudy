from sys import stdin
a, b = map(int, stdin.readline().split())
aa, bb = a, b

while bb != 0:
    aa, bb = bb, aa%bb

print(a*b//aa)
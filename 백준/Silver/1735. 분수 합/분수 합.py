from sys import stdin

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())

e = a*d + c*b
f = b*d
g = gcd(e, f)

print(e//g, f//g)
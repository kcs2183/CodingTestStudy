import sys

n, a, b = map(int, sys.stdin.readline().split())
num_course = []

for _ in range(10):
    x, y = map(int, sys.stdin.readline().split())
    num_course.append((x, y))

for i in range(8-n):
    max_credits = 6
    x, y = num_course[i]

    a += x*3
    b += x*3
    max_credits -= x

    if max_credits > 0:
        if max_credits > y:
            b += y*3
        else:
            b += max_credits*3

if a >= 66 and b >= 130:
    print('Nice')
else:
    print('Nae ga wae')
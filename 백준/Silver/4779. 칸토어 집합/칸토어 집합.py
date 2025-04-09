from sys import stdin

def cantor(i, n):
    if n == 1:
        return
    else:
        arr[i + n//3: i + n//3 *2] = ' ' * (n//3)
        cantor(i, n//3)
        cantor(i + n//3 *2, n//3)

while True:
    try:
        num = int(stdin.readline())
        arr = ['-'] * (3**num)
        cantor(0, 3**num)
        print(''.join(arr))
    except:
        break
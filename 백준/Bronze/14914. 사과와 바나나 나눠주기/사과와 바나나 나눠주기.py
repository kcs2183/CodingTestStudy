def split_fruits(a, b):
    if a < b:
        setting = a
    else:
        setting = b

    for i in range(1, setting+1):
        if a%i == 0 and b%i == 0:
            print(i, int(a/i), int(b/i))

a, b = map(int, input().split())

split_fruits(a, b)
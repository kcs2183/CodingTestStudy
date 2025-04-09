s = input()

length = len(s)
substring = {}

for i in range(length):
    for j in range(i+1, length+1):
        substring[s[i:j]] = 0

print(len(substring))
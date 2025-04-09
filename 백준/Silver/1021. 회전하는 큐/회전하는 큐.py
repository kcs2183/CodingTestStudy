from sys import stdin

n, m = map(int, stdin.readline().split())
pop_num = list(map(int, stdin.readline().split()))
numbers = list(range(1, n+1))
count = 0

for num in pop_num:
    i = numbers.index(num)

    if i < len(numbers) - i:
        count += i
        numbers = numbers[i+1:] + numbers[:i]
    else:
        count += len(numbers) - i
        numbers = numbers[i+1:] + numbers[:i]

print(count)
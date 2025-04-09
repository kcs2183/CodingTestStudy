from sys import stdin
n = int(stdin.readline())
employees = {}

for _ in range(n):
    name, log = stdin.readline().rstrip().split()
    if log == 'enter':
        if name not in employees:
            employees[name] = log
    else:
        if name in employees:
            del employees[name]

print(*sorted(employees, reverse=True), sep='\n')
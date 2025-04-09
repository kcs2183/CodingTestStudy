from sys import stdin

n, k = map(int, stdin.readline().split())
people = [i+1 for i in range(n)]
index = k-1
answer = []

for _ in range(n):
    answer.append(people[index])
    del people[index]

    if people:
        index = (index +k -1) % len(people)

print('<' + ', '.join(map(str, answer)) + '>')
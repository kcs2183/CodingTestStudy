from collections import Counter
from sys import stdin

counter = Counter(stdin.readline().strip().upper())

max_count = max(counter.values())
most_letter = [letter for letter, count in counter.items() if count == max_count]

if len(most_letter) > 1:
    print('?')
else:
    print(most_letter[0])
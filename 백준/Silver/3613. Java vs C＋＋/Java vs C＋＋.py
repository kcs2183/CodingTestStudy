import sys
import re

word = sys.stdin.readline().rstrip()

java = r'^[a-z][a-zA-Z]*$'
cpp = r'^[a-z]+(?:_[a-z]+)*$'

if re.fullmatch(java, word):
    result = []
    for c in word:
        if c.isupper():
            result.append('_')
            result.append(c.lower())
        else:
            result.append(c)
    print("".join(result))
elif re.fullmatch(cpp, word):
    parts = word.split('_')
    result = parts[0] + "".join(part.capitalize() for part in parts[1:])
    print(result)
else:
    print("Error!")
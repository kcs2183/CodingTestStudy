import sys
input = sys.stdin.readline

stack = []
while True:
    string = input().rstrip()

    if string == '':
        break
    else:
        if len(string) == 1:
            if string[0] == '.':
                string = ''
                break
            
        for s in string:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')':
                if stack:
                    if stack.pop() == '(':
                        continue
                print('no')
                break
            elif s == ']':
                if stack:
                    if stack.pop() == '[':
                        continue
                print('no')
                break
        else:
            if stack:
                print('no')
            else:
                print('yes')
        
        stack = []
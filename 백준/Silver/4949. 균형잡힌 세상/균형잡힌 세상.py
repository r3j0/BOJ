import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.': break

    stack = []
    done = 1
    for i in range(len(s)):
        if s[i] == '(': stack.append(1)
        elif s[i] == '[': stack.append(2)
        elif s[i] == ')': 
            if len(stack) == 0 or stack[-1] == 2:
                done = 0
                break
            else: stack.pop()
        elif s[i] == ']':
            if len(stack) == 0 or stack[-1] == 1:
                done = 0
                break
            else: stack.pop()
        
    if len(stack) != 0: done = 0
    print('yes' if done == 1 else 'no')
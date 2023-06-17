import sys
input = sys.stdin.readline

string = input().rstrip()
stack = []
for s in string:
    if len(stack) == 0 or s == '(' or stack[-1] == ')': stack.append(s)
    else: stack.pop()
print(len(stack))            
import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

stack_level = 0
max_level = 0
stack = []
for i in range(len(string)):
    if len(stack) == 0:
        stack_level = 0
        stack.append([string[i], stack_level])
    else:
        if (stack[-1][0] == '(' and string[i] == ')') or (stack[-1][0] == ')' and string[i] == '('):
            stack_level = max(stack_level, stack[-1][1]) + 1
            max_level = max(max_level, stack_level)
            stack.pop()
        else:
            if len(stack) != 0: stack[-1][1] = max(stack_level, stack[-1][1])
            stack_level = 0
            stack.append([string[i], stack_level])

if len(stack) != 0: print(-1)
else: print(max_level)
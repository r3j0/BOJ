import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
stack = []

res = 0
for a in arr:
    if len(stack) == 0: stack = [a]
    else:
        if stack[-1] < a:
            stack.append(a)
        else:
            stack = [a]
    
    res = max(res, stack[-1] - stack[0])

print(res)
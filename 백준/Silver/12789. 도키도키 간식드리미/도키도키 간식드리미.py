import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
stack = []
now = 1
for a in arr:
    while len(stack) > 0 and stack[-1] == now:
        now += 1
        stack.pop()
    
    if a == now: now += 1
    else: stack.append(a)
done = 1
while stack:
    if stack[-1] == now:
        now += 1
    else:
        done = 0
        break
    stack.pop()

if done: print('Nice')
else: print('Sad')
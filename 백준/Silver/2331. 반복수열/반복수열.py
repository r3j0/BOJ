import sys
input = sys.stdin.readline

a, p = map(int, input().rstrip().split())
S = set()
S.add(a)
now = a
stack = [a]
while True:
    go = 0
    for gogo in list(str(now)):
        go += int(gogo)**p
    
    Ssize = len(S)
    S.add(go)
    if Ssize == len(S):
        while stack[-1] != go:
            stack.pop()
        stack.pop()
        break
    else:
        stack.append(go)
        now = go
print(len(stack))
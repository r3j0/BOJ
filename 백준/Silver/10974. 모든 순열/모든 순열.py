import sys
input = sys.stdin.readline

n = int(input().rstrip())

def backtracking(now):
    global n
    if len(now) == n:
        print(' '.join(map(str, now)))
        return
    
    for i in range(1, n+1):
        if i not in now:
            now.append(i)
            backtracking(now)
            now.pop()

backtracking([])

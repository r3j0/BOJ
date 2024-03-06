import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()

def backtracking(now):
    if len(now) == m:
        print(' '.join(map(str, now)))
        return
    
    for i in range(n):
        now.append(arr[i])
        backtracking(now)
        now.pop()

backtracking([])
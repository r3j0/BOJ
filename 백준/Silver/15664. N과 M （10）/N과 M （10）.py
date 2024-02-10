import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()
dic = {}
def backtracking(now, start):
    if len(now) == m:
        now_str = '_'.join(map(str, now))
        if dic.get(now_str, -1) == -1:
            print(' '.join(map(str, now)))
            dic[now_str] = 1
        return
    
    for i in range(start, len(arr)):
        backtracking(now + [arr[i]], i+1)

backtracking([], 0)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

result = 0
def backtracking(now, cnt):
    global n
    global result
    if cnt == n - 2:
        result = max(result, now)
        return
    
    for i in range(1, n - 1 - cnt):
        f = arr[i-1]
        s = arr[i+1]
        go = arr[i]
        del arr[i]
        backtracking(now + (f * s), cnt + 1)
        arr.insert(i, go)

backtracking(0, 0)

print(result)
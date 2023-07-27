import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

result = 0
def backtracking(now, start):
    global n
    global s
    global arr
    global result
    if now == s and start != 0:
        result += 1
    
    for i in range(start, n):
        backtracking(now + arr[i], i+1)

backtracking(0, 0)
print(result)
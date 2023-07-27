import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

result_now = 1
result = []
def backtracking(now, nowarr):
    global n
    global k
    global result_now
    global result

    if now == n:
        if k == result_now:
            result.extend(nowarr)
        result_now += 1
        return
    
    for i in [1, 2, 3]:
        if now + i <= n:
            nowarr.append(i)
            backtracking(now + i, nowarr)
            del nowarr[-1]

backtracking(0, [])
if len(result) == 0: print(-1)
else: print('+'.join(map(str, result)))
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:(-x[0], x[1]))
result = 0
for ps, pe in arr:
    if arr[4][0] != ps: continue
    if arr[4][1] < pe: result += 1
print(result)
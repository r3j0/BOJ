import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

result = -1
def backtracking(start, muls, sums):
    global n
    global result
    if not (start == 0 and muls == 0 and sums == 0):
        if result == -1: result = abs(muls - sums)
        else: result = min(result, abs(muls - sums))

    for i in range(start, n):
        backtracking(i+1, (muls if muls != 0 else 1) * arr[i][0], sums + arr[i][1])

backtracking(0, 0, 0)
print(result)
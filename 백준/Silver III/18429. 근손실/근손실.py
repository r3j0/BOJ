import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

result = 0
def backtracking(now, power):
    global n
    global result
    global arr
    if sum(now) == n:
        result += 1
        return

    for i in range(n):
        if now[i] == 0 and power + arr[i] >= 500:
            now[i] = 1
            backtracking(now, power + arr[i] - k)
            now[i] = 0


backtracking([0 for _ in range(n)], 500 - k)
print(result)
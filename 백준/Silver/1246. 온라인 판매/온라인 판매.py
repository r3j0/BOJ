import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(m)]
arr.sort()
res = 0
res_i = 0
for i in range(arr[0]):
    if res < i * min(n, m):
        res_i = i
        res = i * min(n, m)
for i in range(m):
    if res < arr[i] * (min(n, m - i)):
        res_i = arr[i]
        res = arr[i] * (min(n, m - i))
print(res_i, res)
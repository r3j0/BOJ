import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()
activate_num = 0
res = 0
for i in range(n):
    res += arr[i] * activate_num
    if activate_num < k:
        activate_num += 1
print(res)
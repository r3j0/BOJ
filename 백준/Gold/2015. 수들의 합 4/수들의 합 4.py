# 2015 : 수들의 합 4
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

now_sum = arr[0]
res = 0 if now_sum != k else 1
dic = {arr[0]:1}

for i in range(1, n):
    now_sum += arr[i]
    if now_sum == k:
        res += 1
    res += dic.get(now_sum - k, 0)

    if not dic.get(now_sum):
        dic[now_sum] = 1
    else:
        dic[now_sum] += 1

print(res)
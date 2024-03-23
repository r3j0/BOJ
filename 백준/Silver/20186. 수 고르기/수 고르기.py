# 20186 : 수 고르기
# 알아서 잘 합니다.

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
now_arr = []
for i in range(n):
    now_arr.append([arr[i], i])

now_arr.sort(key=lambda x:(-x[0], x[1]))

res_arr = []
for i in range(k):
    res_arr.append(now_arr[i])

res_arr.sort(key=lambda x:x[1])

res = 0
for i in range(k):
    res += res_arr[i][0] - i

print(res)
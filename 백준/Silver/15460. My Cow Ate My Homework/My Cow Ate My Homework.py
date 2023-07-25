# 1개를 먹음
# 1 9 2 7
# 1 제외
# 9 2 7 -> 평균 6

# 2개를 먹음
# 9 2 7
# 2 제외
# 9 7 -> 평균 8

# 3개를 먹음
# 2 7
# 2 제외
# 7 -> 평균 7

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

prefixSum = [0]
for a in arr: prefixSum.append(a+prefixSum[-1])

prefixMin = []
for a in range(n):
    if a == 0: prefixMin.append(arr[n-1-a])
    else:
        prefixMin.append(min(prefixMin[-1], arr[n-1-a]))

prefixMin.reverse()

result = 0
result_k = []
result_avail = 0
for k in range(1, n-1):
    #print(prefixSum[-1], prefixSum[k], prefixMin[k], n-1-k)
    now = ((prefixSum[-1] - prefixSum[k]) - prefixMin[k]) / (n-1-k)
    if result_avail == 0 or result < now:
        result = now
        result_k = [k]
        result_avail = 1
    elif result_avail == 1 and result == now:
        result_k.append(k)

for k in result_k: print(k)
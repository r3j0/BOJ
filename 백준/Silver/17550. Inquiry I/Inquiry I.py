import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

prefix_sum = [0]
prefix_sum2 = [0]

for a in arr:
    prefix_sum.append(prefix_sum[-1] + a)
    prefix_sum2.append(prefix_sum2[-1] + a**2)

max_value = 0
for i in range(1, n+1):
    max_value = max(max_value, prefix_sum2[i] * (prefix_sum[-1] - prefix_sum[i]))

print(max_value)
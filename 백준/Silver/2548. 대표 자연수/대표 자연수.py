import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
res_num = arr[0]
res_value = 0
for i in range(n):
    if i == 0:
        for j in range(1, n):
            res_value += abs(arr[0] - arr[j])
    else:
        now = 0
        for j in range(n):
            now += abs(arr[i] - arr[j])
        if res_value > now:
            res_num = arr[i]
            res_value = now
        elif res_value == now and res_num > arr[i]:
            res_num = arr[i]

print(res_num)
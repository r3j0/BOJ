import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(sorted(list(map(int, input().rstrip().split()))))
min_value = arr[0] + arr[-1]
for i in range(1, n):
    min_value = min(min_value, arr[i]+arr[-(1+i)])
print(min_value)
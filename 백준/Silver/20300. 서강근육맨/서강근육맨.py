import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
if n % 2 == 1:
    max_value = arr[-1]
    for i in range((n-1)//2):
        max_value = max(max_value, arr[i] + arr[(n-2) - i])
    print(max_value)
else:
    max_value = arr[0] + arr[-1]
    for i in range(1, n//2):
        max_value = max(max_value, arr[i] + arr[n-1-i])
    print(max_value)
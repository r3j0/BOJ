import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

if arr[1] - arr[0] == arr[2] - arr[1]:
    print(arr[-1] + (arr[1] - arr[0]))
else:
    print(arr[-1] * (arr[1] // arr[0]))
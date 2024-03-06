import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort(reverse=True)
for i in range(1, n):
    arr[0] += arr[i]/2

print(arr[0])
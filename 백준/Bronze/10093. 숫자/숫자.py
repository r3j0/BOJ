import sys
input = sys.stdin.readline

arr = sorted(map(int, input().rstrip().split()))
print(max(0, arr[1] - arr[0] - 1))
for i in range(arr[0] + 1, arr[1]):
    print(i, end=' ')
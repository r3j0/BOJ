import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

for i in range(n):
    arr[i] *= (i+1)

print(arr[0], end=' ')
for i in range(1, n):
    print(arr[i] - arr[i-1], end=' ')
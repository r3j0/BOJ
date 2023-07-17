import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
m = int(input().rstrip())

now = n
go = 1

while go != m:
    go *= 2
    now //= 2

for start in range(n//now):
    arr[start*now:start*now+now] = sorted(arr[start*now:start*now+now])
print(' '.join(map(str, arr)))
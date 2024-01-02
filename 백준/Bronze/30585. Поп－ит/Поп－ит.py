import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [0, 0]
for _ in range(n):
    a = list(input().rstrip())
    arr[0] += a.count('0')
    arr[1] += a.count('1')
print(min(arr))
import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

now = 0
while arr[now] >= x:
    now = (now + 1) % n
    x += 1

print(now + 1)
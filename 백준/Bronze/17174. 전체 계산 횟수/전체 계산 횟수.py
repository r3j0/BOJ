import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
cnt = 0
last = n
while last >= m:
    cnt += last
    last //= m

print(cnt + last)
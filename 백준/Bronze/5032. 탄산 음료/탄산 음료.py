import sys
input = sys.stdin.readline

e, f, c = map(int, input().rstrip().split())
cnt = (e + f) // c
left = (e + f) % c + cnt

while left >= c:
    now = left // c
    cnt += now
    left %= c
    left += now

print(cnt)
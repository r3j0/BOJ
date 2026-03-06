# 3079 : 입국심사
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]

s = 1
e = max(arr) * m

while s < e:
    mid = (s + e) // 2
    now = 0
    for a in arr:
        now += mid // a
    
    if now < m:
        s = mid + 1
    elif now >= m:
        e = mid

print(s)
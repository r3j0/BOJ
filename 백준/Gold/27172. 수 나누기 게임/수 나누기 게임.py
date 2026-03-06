# 27172 : 수 나누기 게임
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

num = [False for _ in range(1000001)]
for a in arr:
    num[a] = True

narr = [0 for _ in range(1000001)]
for i in range(1, 500001):
    j = 2
    while i * j <= 1000000:
        if num[i] and num[i*j]: 
            narr[i] += 1
            narr[i*j] -= 1
        j += 1
    
ans = []
for a in arr:
    ans.append(narr[a])

print(' '.join(map(str, ans)))
# 34073 : DORO
import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
ans = []
for a in arr:
    ans.append(a + 'DORO')
print(' '.join(ans))
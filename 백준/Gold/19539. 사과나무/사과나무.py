import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
#n = len(arr)

cnt = [0, 0]
for a in arr:
    cnt[0] += a // 2
    cnt[1] += a % 2

if cnt[0] - cnt[1] >= 0 and (cnt[0] - cnt[1]) * 2 % 3 == 0: print('YES')
else: print('NO')
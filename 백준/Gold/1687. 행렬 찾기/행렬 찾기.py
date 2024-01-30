import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

sums = [[0 for _ in range(m+1)] for _ in range(n+1)]
# y, x 에 0이 연속된.. 그거 거시기 뭐냐
# [y, x] 위쪽까지 연속한 거 [y, x] 왼쪽까지 연속한 거

for i in range(n):
    for j in range(m):
        if maps[i][j] == '0':
            sums[i+1][j+1] = sums[i+1][j] + 1
#for i in range(n+1): print(sums[i])
result = 0
for i in range(n):
    for j in range(m):
        if sums[i+1][j+1] > 0:
            now_cnt = i - 1
            now_col = sums[i+1][j+1]
            while now_cnt >= 0 and sums[now_cnt + 1][j+1] > 0:
                now_col = min(sums[now_cnt + 1][j+1], now_col)
                now_cnt -= 1
            
            
                result = max(result, (i - now_cnt) * (now_col))
            result = max(result, (i - now_cnt) * (now_col))

print(result)
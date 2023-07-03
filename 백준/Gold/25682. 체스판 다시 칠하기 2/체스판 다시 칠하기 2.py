import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

# 1. leftup white
# 2. leftup black

white_prefixSum = [[0 for _ in range(m)] for _ in range(n)]
black_prefixSum = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i > 0: 
            white_prefixSum[i][j] += white_prefixSum[i-1][j]
            black_prefixSum[i][j] += black_prefixSum[i-1][j]
        if j > 0: 
            white_prefixSum[i][j] += white_prefixSum[i][j-1]
            black_prefixSum[i][j] += black_prefixSum[i][j-1]
        if i > 0 and j > 0: 
            white_prefixSum[i][j] -= white_prefixSum[i-1][j-1]
            black_prefixSum[i][j] -= black_prefixSum[i-1][j-1]

        if (i % 2 == j % 2 and maps[i][j] == 'W') or (i % 2 != j % 2 and maps[i][j] == 'B'):
            white_prefixSum[i][j] += 1
        if (i % 2 == j % 2 and maps[i][j] == 'B') or (i % 2 != j % 2 and maps[i][j] == 'W'):
            black_prefixSum[i][j] += 1

mins = 0
mins_avail = 0

i_idx = 0
while i_idx + k <= n:
    j_idx = 0
    while j_idx + k <= m:
        now_white = white_prefixSum[i_idx+k-1][j_idx+k-1]
        now_black = black_prefixSum[i_idx+k-1][j_idx+k-1]
        if i_idx > 0:
            now_white -= white_prefixSum[i_idx-1][j_idx+k-1]
            now_black -= black_prefixSum[i_idx-1][j_idx+k-1]
        if j_idx > 0:
            now_white -= white_prefixSum[i_idx+k-1][j_idx-1]
            now_black -= black_prefixSum[i_idx+k-1][j_idx-1]
        if i_idx > 0 and j_idx > 0:
            now_white += white_prefixSum[i_idx-1][j_idx-1]
            now_black += black_prefixSum[i_idx-1][j_idx-1]
        
        if mins_avail == 0 or (mins > (k**2)-now_white or mins > (k**2)-now_black):
            mins_avail = 1
            mins = min((k**2)-now_white, (k**2)-now_black)
        
        j_idx += 1
    i_idx += 1

print(mins)
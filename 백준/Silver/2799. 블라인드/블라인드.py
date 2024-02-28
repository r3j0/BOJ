import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(1+(m*5))]
res = [0 for _ in range(5)]
for i in range(m):
    for j in range(n):
        start_y = 1+(i*5)
        start_x = 1+(j*5)

        cnt = 0
        for k in range(4):
            if arr[start_y+k][start_x] == '*': cnt += 1
        res[cnt] += 1
print(' '.join(map(str, res)))
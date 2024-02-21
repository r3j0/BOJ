import sys
input = sys.stdin.readline

res = [list(map(int, input().rstrip().split())) for _ in range(5)]
arr = []
for _ in range(5):
    a = list(map(int, input().rstrip().split()))
    arr.extend(a)

rescnt = 0
result = 0
gocnt = 1
for aval in arr:
    for i in range(5):
        for j in range(5):
            if res[i][j] == aval:
                res[i][j] = 0

                # 가로
                cnt = 0
                for jidx in range(5):
                    if res[i][jidx] == 0: cnt += 1
                if cnt == 5: rescnt += 1
                # 세로
                cnt = 0
                for iidx in range(5):
                    if res[iidx][j] == 0: cnt += 1
                if cnt == 5: rescnt += 1
                # 대각 /
                if i + j == 4:
                    cnt = 0
                    for k in range(5):
                        if res[k][4-k] == 0: cnt += 1
                    if cnt == 5: rescnt += 1
                # 대각 \
                if i - j == 0:
                    cnt = 0
                    for k in range(5):
                        if res[k][k] == 0: cnt += 1
                    if cnt == 5: rescnt += 1
    if rescnt >= 3 and result == 0:
        result = gocnt
    gocnt += 1
print(result)


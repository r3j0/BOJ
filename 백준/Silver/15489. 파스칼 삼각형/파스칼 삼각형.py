# 15489 : 파스칼 삼각형
# 테이블을 미리 만들어 합을 구합니다.

import sys
input = sys.stdin.readline

r, c, w = map(int, input().rstrip().split())
arr = [[0 for _ in range(35)] for _ in range(35)]
arr[1][1] = 1

for i in range(2, r+w+1):
    for j in range(1, i+1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

res = 0
for i in range(r, r+w):
    for j in range(c, c+(i-r+1)):
        res += arr[i][j]

print(res)
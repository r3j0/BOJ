import sys 
input = sys.stdin.readline

h, w = map(int, input().rstrip().split())
n = int(input().rstrip())
paper = [list(map(int, input().rstrip().split())) for _ in range(n)]

res = 0
for i in range(n-1):
    for j in range(i+1, n):
        # 1. i 정방향 / j 정방향
        # 1-1. 상하
        if paper[i][0] + paper[j][0] <= h and max(paper[i][1], paper[j][1]) <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 1-2. 좌우
        if max(paper[i][0], paper[j][0]) <= h and paper[i][1] + paper[j][1] <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 2. i 정방향 / j 역방향
        # 2-1. 상하
        if paper[i][0] + paper[j][1] <= h and max(paper[i][1], paper[j][0]) <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 2-2. 좌우
        if max(paper[i][0], paper[j][1]) <= h and paper[i][1] + paper[j][0] <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 3. i 역방향 / j 정방향
        # 3-1. 상하
        if paper[i][1] + paper[j][0] <= h and max(paper[i][0], paper[j][1]) <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 3-2. 좌우
        if max(paper[i][1], paper[j][0]) <= h and paper[i][0] + paper[j][1] <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 4. i 역방향 / j 역방향
        # 4-1. 상하
        if paper[i][1] + paper[j][1] <= h and max(paper[i][0], paper[j][0]) <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

        # 4-2. 좌우
        if max(paper[i][1], paper[j][1]) <= h and paper[i][0] + paper[j][0] <= w:
            res = max(res, paper[i][0] * paper[i][1] + paper[j][0] * paper[j][1])

print(res)
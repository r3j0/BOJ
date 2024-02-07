import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
order = [list(map(int, input().rstrip().split())) for _ in range(m)]

# 0 1 2
# 0이 n - 1 이하라면 전체 1 증가는 확정
# 그 이상일 떄는 1 2 해당 선까지 증가

plus = [0 for _ in range(n-1)]
edge = [1 for _ in range(2*n-1)]

for day in range(m):
    day_step = 0
    for i in range(n-1, -1, -1):
        while order[day][day_step] == 0:
            day_step += 1
        edge[n - 1 - i] += day_step
        order[day][day_step] -= 1

    for j in range(1, n):
        while order[day][day_step] == 0:
            day_step += 1
        edge[n - 1 + j] += day_step
        order[day][day_step] -= 1
        plus[j-1] += day_step
    

for j in range(n-1, 2*n-1):
    print(edge[j], end=' ')
print()
for i in range(1, n):
    print(edge[n-1-i], end=' ')
    for k in range(n-1):
        print(1 + plus[k], end=' ')
    print()
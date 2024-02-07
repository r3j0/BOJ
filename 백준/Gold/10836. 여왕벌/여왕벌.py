import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
order = [[0] + list(map(int, input().rstrip().split())) for _ in range(m)]

# 0 1 2
# 0이 n - 1 이하라면 전체 1 증가는 확정
# 그 이상일 떄는 1 2 해당 선까지 증가

edge_plus = [0 for _ in range(2*n-1)]

for day in range(m):
    order[day][2] += order[day][1]
    order[day][3] += order[day][2]
    if order[day][1] != order[day][2]:
        edge_plus[order[day][1]] += 1
    if order[day][2] != order[day][3]:
        if order[day][1] == order[day][2]:
            edge_plus[order[day][1]] += 2
        else:
            edge_plus[order[day][2]] += 1

for i in range(1, 2*n-1):
    edge_plus[i] += edge_plus[i-1]

for i in range(2*n-1): edge_plus[i] += 1

print(' '.join(map(str, edge_plus[n-1:])))
res = ' '.join(map(str, edge_plus[n:]))
for i in range(n-2, -1, -1):
    print(edge_plus[i], end=' ')
    print(res)
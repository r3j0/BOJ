import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    dots = [list(map(int, input().rstrip().split())) for _ in range(4)]
    cnt = 0
    for i in range(4):
        dist = []
        for j in range(4):
            if i == j: continue
            dist.append(((dots[i][0] - dots[j][0])**2) + ((dots[i][1] - dots[j][1])**2))
        dist.sort()
        if dist[0] == dist[1] and dist[0] * 2 == dist[2]: cnt += 1
    print(1 if cnt == 4 else 0)
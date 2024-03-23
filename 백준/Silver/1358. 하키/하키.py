# 1358 : 하키
# 1. 정사각형 안에 있는지 확인합니다.
# 2. 원 안에 있는지 확인합니다. (원 중심을 기준으로 거리를 구해 R 보다 작거나 같은지)

import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().rstrip().split())
people = [list(map(int, input().rstrip().split())) for _ in range(p)]
res = 0

def Distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)

for i in range(p):
    if ((x <= people[i][0] <= x + w) and (y <= people[i][1] <= y + h)) or (Distance(x, y + (h//2), people[i][0], people[i][1]) <= h//2 or Distance(x + w, y + (h//2), people[i][0], people[i][1]) <= h//2): res += 1

print(res)
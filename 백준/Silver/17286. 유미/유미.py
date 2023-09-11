import sys
import math
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())
pos = [list(map(int, input().rstrip().split())) for _ in range(3)]

def dist(x1, y1, x2, y2):
    return math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2))

min_distance = float('inf')
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i == j or j == k or i == k:
                continue
            
            min_distance = min(min_distance, dist(x, y, pos[i][0], pos[i][1]) + dist(pos[i][0], pos[i][1], pos[j][0], pos[j][1]) + dist(pos[j][0], pos[j][1], pos[k][0], pos[k][1]))
    
print(int(min_distance))
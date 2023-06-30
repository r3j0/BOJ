import sys
input = sys.stdin.readline

n = int(input().rstrip())
dist = list(map(int, input().rstrip().split()))
cost = list(map(int, input().rstrip().split()))

now = 0
now_cost = 0

for i in range(n):
    if i == 0:
        now_cost += dist[i] * cost[i]
    elif i != n - 1:
        if cost[now] >= cost[i]:
            now = i
        
        now_cost += dist[i] * cost[now]

print(now_cost)
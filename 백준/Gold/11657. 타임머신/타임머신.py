import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))

cycle = False
def bellman_ford(start):
    global cycle
    distances = [float('inf') for _ in range(n+1)]
    distances[start] = 0
    
    for i in range(n):
        for st, des, we in edges:
            if distances[st] != float('inf') and distances[des] > distances[st] + we:
                if i == n - 1: cycle = True
                distances[des] = distances[st] + we
    return distances

result = bellman_ford(1)
if cycle: print(-1)
else:
    for i in range(2, n+1):
        print(result[i] if result[i] != float('inf') else -1)      

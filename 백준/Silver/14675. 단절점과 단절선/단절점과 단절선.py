import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v = int(input().rstrip())
graph = [{} for _ in range(v+1)]
edges = [list(map(int, input().rstrip().split())) for _ in range(v-1)]
for e in edges:
    a, b = e
    graph[a][b] = 1
    graph[b][a] = 1

q = int(input().rstrip())
for _ in range(q):
    t, k = map(int, input().rstrip().split())
    if t == 1: # k가 단절점인가?
        if len(list(graph[k].keys())) != 1: print('yes')
        else: print('no')
    else: # k가 단절선인가?
        print('yes')
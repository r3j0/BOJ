import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000)

v, e = map(int, input().rstrip().split())
graph = [{} for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0 for _ in range(v+1)]
visited_cnt = 1

result = []
def dfs(now, parent):
    global visited_cnt
    visited[now] = visited_cnt
    visited_cnt += 1
    num = visited[now]

    for next in list(graph[now].keys()):
        if next == parent: continue
        if visited[next] == 0:
            low = dfs(next, now)
            num = min(low, num)

            if ((low > visited[now])):
                result.append([min(now, next), max(now, next)])
        else:
            num = min(num, visited[next])

    return num

for i in range(1, v+1):
    if visited[i] == 0:
        dfs(i, 0)

print(len(result))
result.sort()
for r in result: print(' '.join(map(str, r)))
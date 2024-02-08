import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

v, e = map(int, input().rstrip().split())
graph = [{} for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0 for _ in range(v+1)]
visited_cnt = 1

result = [0 for _ in range(v+1)]
def dfs(now, isRoot):
    global visited_cnt
    visited[now] = visited_cnt
    visited_cnt += 1

    num = visited[now]
    child = 0

    for next in list(graph[now].keys()):
        if visited[next] == 0:
            child += 1
            low = dfs(next, 0)
            num = min(low, num)

            if ((isRoot == 0) and (low >= visited[now])):
                result[now] = 1
        else:
            num = min(num, visited[next])
    
    if isRoot == 1 and child > 1:
        result[now] = 1

    return num

for i in range(1, v+1):
    if visited[i] == 0:
        dfs(i, 1)

res_cnt = 0
res_arr = []
for i in range(1, v+1):
    if result[i] == 1:
        res_cnt += 1
        res_arr.append(i)

print(res_cnt)
print(' '.join(map(str, res_arr)))
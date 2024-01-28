import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
friends = [{} for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    friends[a][b] = 1
    friends[b][a] = 1

visited = [0 for _ in range(n)]

def backtracking(now, cnt):
    result = cnt
    if cnt == 4: return cnt
    visited[now] = 1

    for k in list(friends[now].keys()):
        if visited[k] == 0:
            result = max(result, backtracking(k, cnt+1))

    visited[now] = 0
    return result

done = 0
for i in range(n):
    result = backtracking(i, 0)
    if result == 4:
        done = 1
        break

print(done)
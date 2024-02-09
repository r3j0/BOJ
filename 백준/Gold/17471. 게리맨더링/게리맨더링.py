import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
graph = [{} for _ in range(n+1)]
for i in range(n):
    nodes = list(map(int, input().rstrip().split()))[1:]
    for j in nodes:
        graph[i+1][j] = 1
result = -1
def backtracking(now, cur):
    global n
    global result
    if now == n:
        cnt = [0, 0]
        for i in range(n):
            cnt[cur[i]-1] += 1
        
        if min(cnt) == 0: return

        citizen_cnt = [0, 0]
        arr_cnt = [0, 0]
        vis = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if vis[i] == 0:
                vis[i] = 1
                queue = deque()
                arr_cnt[cur[i-1]-1] += 1
                citizen_cnt[cur[i-1]-1] += arr[i-1]
                queue.append(i)
                while queue:
                    nowq = queue.popleft()
                    for next in list(graph[nowq].keys()):
                        if vis[next] == 0 and cur[next-1] == cur[nowq-1]:
                            vis[next] = 1
                            citizen_cnt[cur[next-1]-1] += arr[next-1]
                            queue.append(next)
        
        if min(arr_cnt) == 1 and max(arr_cnt) == 1:
            if result == -1:
                result = abs(citizen_cnt[0] - citizen_cnt[1])
            else:
                result = min(result, abs(citizen_cnt[0] - citizen_cnt[1]))

        return

    cur[now] = 1
    backtracking(now+1, cur)
    cur[now] = 2
    backtracking(now+1, cur)

backtracking(0, [0 for _ in range(n)])
print(result)
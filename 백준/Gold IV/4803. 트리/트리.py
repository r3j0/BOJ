import sys
from collections import deque
input = sys.stdin.readline

tc = 1
while True:
    n, m = map(int, input().rstrip().split())
    if n == 0 and m == 0: break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    vis = [0 for _ in range(n+1)]
    cnt = 0
    for i in range(1, n+1):
        if vis[i] == 0: 
            cnt += 1
            ncnt = 1
            mcnt = 0
            vis[i] = cnt
            queue = deque()
            queue.append(i)
            done = True
            while queue:
                now = queue.popleft()
                vis[now] = cnt
                tt = 0
                for next in graph[now]:
                    if vis[next] != cnt:
                        queue.append(next)
                    else:
                        if now == next: done = False
                        tt += 1
                        if tt > 1:
                            done = False

            if done == False: 
                cnt -= 1
    
    if cnt > 1: print('Case %d: A forest of %d trees.'%(tc, cnt))
    elif cnt == 1: print('Case %d: There is one tree.'%(tc))
    else: print('Case %d: No trees.'%(tc))

    tc += 1
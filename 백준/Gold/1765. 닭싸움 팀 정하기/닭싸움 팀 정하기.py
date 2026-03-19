# 1765 : 닭싸움 팀 정하기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
f_edges = [set() for _ in range(n+1)]
e_edges = [set() for _ in range(n+1)]
for _ in range(m):
    mode, p, q = input().rstrip().split()
    p = int(p)
    q = int(q)

    if mode == 'F':
        f_edges[p].add(q)
        f_edges[q].add(p)
    else:
        e_edges[p].add(q)
        e_edges[q].add(p)

# 내 친구의 친구는 내 친구이다.
# 내 원수의 원수는 내 친구이다.

# F p q : 친구
# E p q : 원수

# 가능한 최대 팀 개수

# 원수 엣지가 있다면, 그 다음 원수 엣지랑 전부 친구 엣지 만들기

# 1. 한 친구마다. 원수 엣지가 있는지 보기
for i in range(1, n+1):
    # 2. 원수 엣지가 있다면, 원수의 원수들과 친구 엣지 만들기
    for e in e_edges[i]:
        for ne in e_edges[e]:
            if i == ne: continue
            f_edges[i].add(ne)
            f_edges[ne].add(i)
    
# 3. 친구 엣지들로 BFS 탐색
cnt = 0
vis = [False for _ in range(n+1)]

for i in range(1, n+1):
    if not vis[i]:
        queue = deque()
        queue.append(i)
        vis[i] = True

        while queue:
            now = queue.popleft()
            for nex in f_edges[now]:
                if not vis[nex]:
                    queue.append(nex)
                    vis[nex] = True
        
        cnt += 1

print(cnt)
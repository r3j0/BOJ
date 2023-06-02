import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
cells = {}

for i in range(m):
    p, q = map(int, input().rstrip().split())
    graph[p-1].append(q-1)

grundy = [[-1 for _ in range(n)] for _ in range(n)]

def mex(S):
    S = sorted(S)
    for l in range(len(S)):
        if l != S[l]: return l
    return len(S)

def g(n1, n2):
    if grundy[n1][n2] != -1: return grundy[n1][n2]
    if grundy[n2][n1] != -1: return grundy[n2][n1]

    S = set()
    if n1 == n2:
        for e in graph[n1]:
            S.add(grundy[e][e] if grundy[e][e] != -1 else g(e, e))
    else:
        for e1 in graph[n1]:
            S.add(grundy[e1][n2] if grundy[e1][n2] != -1 else g(e1, n2))
        for e2 in graph[n2]:
            S.add(grundy[n1][e2] if grundy[n1][e2] != -1 else g(n1, e2))

    grundy[n1][n2] = mex(S)
    grundy[n2][n1] = grundy[n1][n2]
    return grundy[n1][n2]

k = int(input().rstrip())
for i in range(k):
    v, c = map(int, input().rstrip().split())
    if cells.get(c): cells[c].append(v-1)
    else: cells[c] = [v-1]

result = 0
for v in cells.values():
    if len(v) == 1: result ^= g(v[0], v[0])
    else: result ^= g(min(v), max(v))

print('Cheol' if result == 0 else 'Young')
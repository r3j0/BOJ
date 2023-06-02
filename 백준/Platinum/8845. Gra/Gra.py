import sys
input = sys.stdin.readline

n1, m1 = map(int, input().rstrip().split())
graph1 = [[] for _ in range(n1)]
grundy1 = [-1 for _ in range(n1)]
for _ in range(m1):
    a, b = map(int, input().rstrip(). split())
    a -= 1
    b -= 1
    graph1[a].append(b)

n2, m2 = map(int, input().rstrip().split())
graph2 = [[] for _ in range(n2)]
grundy2 = [-1 for _ in range(n2)]
for _ in range(m2):
    a, b = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    graph2[a].append(b)

def mex(S):
    S = sorted(S)
    for l in range(len(S)):
        if l != S[l]: return l
    return len(S)

def g1(n):
    global grundy1
    if grundy1[n] != -1: return grundy1[n]

    S = set()
    for i in graph1[n]:
        S.add(grundy1[i] if grundy1[i] != -1 else g1(i))
    
    grundy1[n] = mex(S)
    return grundy1[n]

def g2(n):
    global grundy2
    if grundy2[n] != -1: return grundy2[n]
    
    S = set()
    for i in graph2[n]:
        S.add(grundy2[i] if grundy2[i] != -1 else g2(i))

    grundy2[n] = mex(S)
    return grundy2[n]

q = int(input().rstrip())
for _ in range(q):
    x, y = map(int, input().rstrip().split())
    result = g1(x-1)^g2(y-1)
    if result == 0: print('P')
    else: print('W')
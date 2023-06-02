import sys
input = sys.stdin.readline

def mex(S):
    S = sorted(S)
    for l in range(len(S)):
        if l != S[l]: return l
    return len(S)

def g(n):
    global grundy
    global graph
    if grundy[n] != -1: return grundy[n]

    S = set()
    for i in graph[n]:
        S.add(grundy[i] if grundy[i] != -1 else g(i))
    
    grundy[n] = mex(S)
    return grundy[n]

test = int(input().rstrip())
for t in range(test):
    n = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    edge = list(map(int, input().rstrip().split()))
    graph = [[] for _ in range(n)]
    for i in range(n):
        if edge[i] == 0: continue
        graph[edge[i] - 1].append(i)

    grundy = [-1 for _ in range(n)]

    result = 0
    for i in range(n):
        if nums[i] % 2 == 1:
            result ^= g(i)

    print('Case #%d:'%(t+1), 'first' if result != 0 else 'second') 

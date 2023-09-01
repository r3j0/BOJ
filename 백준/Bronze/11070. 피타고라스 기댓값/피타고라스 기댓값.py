import sys
input = sys.stdin.readline

def maxm(a, b):
    if a == -1 and b == -1: return -1
    if a == -1: return b
    if b == -1: return a
    return max(a, b)

def minm(a, b):
    if a == -1 and b == -1: return -1
    if a == -1: return b
    if b == -1: return a
    return min(a, b)

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    score = [[0, 0] for _ in range(n)]
    for _ in range(m):
        a, b, p, q = map(int, input().rstrip().split())
        score[a-1][0] += p
        score[a-1][1] += q
        score[b-1][0] += q
        score[b-1][1] += p
    
    # 아 귀찮아
    maxScore = -1
    minScore = -1

    for i in range(n):
        now = -1
        try:
            now = (score[i][0]**2) / (score[i][0]**2 + score[i][1]**2)
        except:
            now = -1

        if score[i][0] == 0 and score[i][1] == 0: now = 0
        maxScore = maxm(maxScore, now)
        minScore = minm(minScore, now)
    
    print(int(maxScore * 1000) if maxScore != -1 else 0)
    print(int(minScore * 1000) if minScore != -1 else 0)
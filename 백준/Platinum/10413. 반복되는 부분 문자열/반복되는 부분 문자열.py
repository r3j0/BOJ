# 10413 : 반복되는 부분 문자열
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    n = len(s)

    # Suffix Array
    sa = [i for i in range(n)]
    rank = [ord(c) for c in s]
    k = 1
    tmp = [0 for _ in range(n)]

    while True:
        sa.sort(key=lambda i:(rank[i], rank[i+k] if i + k < n else -1))

        tmp[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i-1]
            cur = sa[i]

            prev_key = (rank[prev], rank[prev+k] if prev + k < n else -1)
            cur_key = (rank[cur], rank[cur+k] if cur + k < n else -1)

            tmp[cur] = tmp[prev] + (prev_key != cur_key)
        rank, tmp = tmp, rank

        if rank[sa[-1]] == n - 1: break

        k *= 2
    
    # LCP
    rank_in_sa = [0 for _ in range(n)]
    for i, pos in enumerate(sa):
        rank_in_sa[pos] = i
    lcp = [0 for _ in range(n)]
    h = 0
    for i in range(n):
        r = rank_in_sa[i]
        if r == 0: continue

        j = sa[r-1]
        
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1

        lcp[r] = h
        if h > 0:
            h -= 1
    
    res = 0
    for i in range(1, n):
        res += max(0, lcp[i] - lcp[i-1])
    
    print(res)
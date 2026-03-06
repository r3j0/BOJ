# 3789 : Hidden Password
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    nn, s = input().split()
    nn = int(nn)
    n = nn * 2
    s += s

    # Suffix Array
    k = 1
    tmp = [0 for _ in range(n)]
    sa = [i for i in range(n)]
    rank = [ord(c) for c in s]
    while True:
        sa.sort(key = lambda i:(rank[i], rank[i+k] if i + k < n else -1))

        tmp[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i-1]
            cur = sa[i]

            prev_key = (rank[prev], rank[prev+k] if prev+k < n else -1)
            cur_key = (rank[cur], rank[cur+k] if cur+k < n else -1)

            tmp[cur] = tmp[prev] + (prev_key != cur_key)
        rank, tmp = tmp, rank

        if rank[sa[-1]] == n - 1:
            break

        k *= 2
    
    find = False
    res = 0
    for i in range(n):
        if sa[i] < nn:
            if find:
                if sa[i-1] > sa[i]:
                    res = sa[i]
                else:
                    break
            else:
                find = True
                res = sa[i]
        elif find:
            break
    
    print(res)
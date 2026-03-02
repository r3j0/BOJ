# 9248 : Suffix Array
import sys
input = sys.stdin.readline

s = input().rstrip()

n = len(s)
sa = [i for i in range(n)]
rank = [ord(c) for c in s]
tmp = [0 for _ in range(n)]
k = 1
while True:
    sa.sort(key = lambda i:(rank[i], rank[i+k] if i + k < n else -1))

    tmp[sa[0]] = 0
    for i in range(1, n):
        prev = sa[i-1]
        cur = sa[i]

        prev_key = (rank[prev], rank[prev+k] if prev + k < n else -1)
        cur_key = (rank[cur], rank[cur+k] if cur + k < n else -1)

        tmp[cur] = tmp[prev] + (prev_key != cur_key)
    
    rank, tmp = tmp, rank
    
    if rank[sa[-1]] == n - 1:
        break

    k *= 2

rank_in_sa = [0 for _ in range(n)]
h = 0
lcp = [0 for _ in range(n)]

for i, pos in enumerate(sa):
    rank_in_sa[pos] = i

for i in range(n):
    r = rank_in_sa[i]
    if r == 0: continue

    j = sa[r - 1]
    while i + h < n and j + h < n and s[i + h] == s[j + h]:
        h += 1

    lcp[r] = h

    if h > 0:
        h -= 1

lcp[0] = 'x'

for i in range(n): sa[i] += 1

print(' '.join(map(str, sa)))
print(' '.join(map(str, lcp)))
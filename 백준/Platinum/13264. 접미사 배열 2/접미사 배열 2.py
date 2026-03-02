# 13264 : 접미사 배열 2
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

for i in sa: print(i)
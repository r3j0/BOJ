# 9249 : 최장 공통 부분 문자열
import sys
input = sys.stdin.readline

# 두 문자를 합치고, 중간에 아무거나 넣기?
a = input().rstrip()
b = input().rstrip()
s = a+'X'+b
n = len(s)

# Suffix Array
sa = [i for i in range(n)]
rank = [ord(c) for c in s]
k = 1
tmp = [0 for _ in range(n)]
while True:
    sa.sort(key=lambda i:(rank[i], rank[i+k] if i+k < n else -1))

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

# LCP
rank_in_sa = [0 for _ in range(n)]
lcp = [0 for _ in range(n)]
h = 0

for i, pos in enumerate(sa):
    rank_in_sa[pos] = i

for i in range(n):
    r = rank_in_sa[i]
    if r == 0: continue

    j = sa[r-1]
    while i + h < n and j + h < n and s[i+h] == s[j+h]:
        h += 1
    
    lcp[r] = h

    if h > 0:
        h -= 1

# 최장 공통 부분 문자열
res_len = 0
res_idx = 0
for i in range(n):
    right = rank_in_sa[i]
    if right == 0: continue

    j = sa[right - 1]
    
    if lcp[right] > res_len and ((j > len(a) and i <= len(a)) or
                                 (i > len(a) and j <= len(a))):
        res_len = lcp[right]
        res_idx = i

print(res_len)
print(s[res_idx:res_idx+res_len])
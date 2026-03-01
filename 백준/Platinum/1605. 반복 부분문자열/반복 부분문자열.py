# 1605 : 반복 부분문자열
import sys
input = sys.stdin.readline

l = int(input().rstrip())
s = input().rstrip()

# rank : 접미사 s[i] 의 길이 k의 그룹 번호
rank = [ord(c) for c in s]
# sa : 접미사 시작 인덱스들을 접미사 사전 순으로 정렬한 결과
sa = list(range(l))
# tmp : rank 임시용
tmp = [0 for _ in range(l)]
k = 1

while True:
    # 앞 뒤 덩어리로 잘라서 비교, 만약 부족하면 -1로 맨 앞으로 오게끔
    sa.sort(key = lambda i:(rank[i], rank[i+k] if i + k < l else -1))

    tmp[sa[0]] = 0
    for i in range(1, l):
        prev = sa[i-1]
        cur = sa[i]

        prev_key = (rank[prev], rank[prev+k] if prev + k < l else -1)
        cur_key = (rank[cur], rank[cur+k] if cur + k < l else -1)

        tmp[cur] = tmp[prev] + (prev_key != cur_key)

    rank, tmp = tmp, rank

    if rank[sa[-1]] == l - 1:
        break

    k *= 2

rank_in_sa = [0 for _ in range(l)]
for i, pos in enumerate(sa):
    rank_in_sa[pos] = i

lcp = [0 for _ in range(l)]
h = 0

for i in range(l):
    r = rank_in_sa[i]
    if r == 0: continue

    j = sa[r-1]
    while i + h < l and j + h < l and s[i+h] == s[j+h]:
        h += 1
    
    lcp[r] = h
    if h > 0:
        h -= 1

print(max(lcp))
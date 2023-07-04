import sys
input = sys.stdin.readline

n = int(input())
dic = {}
arr = list(map(int, input().rstrip().split()))
for a in arr:
    if dic.get(a): dic[a] += 1
    else: dic[a] = 1

maxs = 0
for k, v in dic.items():
    if k == v:
        maxs = max(maxs, k)

if maxs == 0 and 0 in list(dic.keys()): print(-1)
else: print(maxs)
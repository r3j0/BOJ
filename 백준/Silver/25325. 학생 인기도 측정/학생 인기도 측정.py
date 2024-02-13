import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(input().rstrip().split())
dic = {}
for a in arr: dic[a] = 0
for _ in range(n):
    narr = list(input().rstrip().split())
    for a in narr: dic[a] += 1

result = list(dic.items())
result.sort(key=lambda x:(-x[1], x[0]))
for r in result: print(r[0], r[1])
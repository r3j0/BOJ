import sys
input = sys.stdin.readline

q = int(input().rstrip())
dic = {}
cnt = 0
for _ in range(q):
    s, p = input().rstrip().split()
    if p == '+':
        if dic.get(s, -1) == -1: dic[s] = 1
        else: dic[s] += 1
    else:
        if dic.get(s, -1) == -1: cnt += 1
        else: 
            if dic[s] == 1: del dic[s]
            else: dic[s] -= 1

for k, v in dic.items():
    cnt += v

print(cnt)
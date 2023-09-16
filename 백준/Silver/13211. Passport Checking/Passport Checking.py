import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = {}
for _ in range(n):
    dic[input().rstrip()] = 1
m = int(input().rstrip())
cnt = 0
for _ in range(m):
    tmp = input().rstrip()
    if dic.get(tmp): cnt += 1
print(cnt)
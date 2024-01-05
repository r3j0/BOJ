import sys
input = sys.stdin.readline

n = int(input().rstrip())
words = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    while len(words[i]) != 12:
        words[i] = ['0'] + words[i]

cand = {}
for j in range(12):
    for i in range(n):
        if 'A' <= words[i][j] <= 'Z':
            cand[words[i][j]] = 0

for j in range(12):
    for i in range(n):
        if 'A' <= words[i][j] <= 'Z':
            cand[words[i][j]] += (10**(11-j))

c = list(cand.items())
c.sort(key=lambda x:(-x[1], x[0]))

used = 9
result = 0
for _, value in c:
    result += value*used
    used -= 1

print(result)
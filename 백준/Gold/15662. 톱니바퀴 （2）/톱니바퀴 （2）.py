import sys
input = sys.stdin.readline

n = int(input().rstrip())
topni = [input().rstrip() for _ in range(n)]
k = int(input().rstrip())

def rotate(top, dir):
    if dir == 1: return top[-1:] + top[:-1]
    else: return top[1:] + top[:1]

def leftGo(now, dir):
    if int(topni[now][2]) ^ int(topni[now+1][6]):
        if now != 0: leftGo(now - 1, 1 if dir == -1 else -1)
        topni[now] = rotate(topni[now], dir)

def rightGo(now, dir):
    if int(topni[now][6]) ^ int(topni[now-1][2]):
        if now != n - 1: rightGo(now + 1, 1 if dir == -1 else -1)
        topni[now] = rotate(topni[now], dir)

for _ in range(k):
    i, dir = map(int, input().rstrip().split())
    if i - 1 != 0: leftGo(i - 2, 1 if dir == -1 else -1)
    if i - 1 != n - 1: rightGo(i, 1 if dir == -1 else -1)
    topni[i - 1] = rotate(topni[i - 1], dir)

cnt = 0
for i in range(n):
    if topni[i][0] == '1': cnt += 1
print(cnt)
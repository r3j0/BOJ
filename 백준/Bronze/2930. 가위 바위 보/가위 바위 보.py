import sys
input = sys.stdin.readline

r = int(input().rstrip())
sanggeun = input().rstrip()
n = int(input().rstrip())
arr = [input().rstrip() for _ in range(n)]

def winScore(sang, frie):
    if sang == 'S':
        if frie == 'S': return 1
        elif frie == 'R': return 0
        else: return 2
    elif sang == 'R':
        if frie == 'S': return 2
        elif frie == 'R': return 1
        else: return 0
    else:
        if frie == 'S': return 0
        elif frie == 'R': return 2
        else: return 1

# 상근이의 점수
nowScore = 0
for i in range(n):
    for j in range(r):
        nowScore += winScore(sanggeun[j], arr[i][j])

print(nowScore)

# 상근이가 얻을 수 있는 최대 점수
maxScore = 0
for i in range(r):
    nowMax = 0
    now = ['S', 'R', 'P']
    for go in now:
        tmpScore = 0
        for j in range(n):
            tmpScore += winScore(go, arr[j][i])
        nowMax = max(nowMax, tmpScore)
    maxScore += nowMax

print(maxScore)
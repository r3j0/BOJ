import sys
input = sys.stdin.readline

E, S, M = map(int, input().rstrip().split())

NE = 1
NS = 1
NM = 1
cnt = 1

while not (NE == E and NS == S and NM == M):
    NE += 1
    NS += 1
    NM += 1

    if (NE > 15): NE = 1
    if (NS > 28): NS = 1
    if (NM > 19): NM = 1
    cnt += 1

print(cnt)
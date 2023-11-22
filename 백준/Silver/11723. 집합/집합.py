import sys
input = sys.stdin.readline

m = int(input().rstrip())
S = [0 for _ in range(21)]
for _ in range(m):
    ope = list(input().rstrip().split())
    if ope[0] == 'add': S[int(ope[1])] = 1
    elif ope[0] == 'remove': S[int(ope[1])] = 0
    elif ope[0] == 'check': print(S[int(ope[1])])
    elif ope[0] == 'toggle': S[int(ope[1])] = 1 if S[int(ope[1])] == 0 else 0
    elif ope[0] == 'all':
        for i in range(1, 21): S[i] = 1
    elif ope[0] == 'empty':
        for i in range(1, 21): S[i] = 0
grundy = [-1 for _ in range(2001)]
grundy[0] = 0
grundy[1] = 1
grundy[2] = 1
grundy[3] = 1

def mex(S):
    S = sorted(S)
    for l in range(len(S)):
        if l != S[l]: return l
    
    return len(S)

for i in range(4, 2001):
    S = set()
    for j in range(0, (i-1)//2+1):
        first = j-2 if j-2 >= 0 else 0
        second = i-1-j-2 if i-1-j-2 >= 0 else 0
        S.add(grundy[first]^grundy[second])

    grundy[i] = mex(S)

"""
for i in range(0, 21):
    print(grundy[i], end=', ')
"""

import sys
input = sys.stdin.readline
n = int(input())
if grundy[n] == 0: print(2)
else: print(1)

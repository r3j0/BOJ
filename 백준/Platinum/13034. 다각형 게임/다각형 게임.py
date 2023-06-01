import sys      
input = sys.stdin.readline

grundy = [-1] * 1001
grundy[0] = 0
grundy[1] = 0
grundy[2] = 1

def mex(l):
    l = sorted(l)
    for i in range(len(l)):
        if i != l[i]:
            return i
    return len(l)

n = int(input().rstrip())

for i in range(3, n+1):
    s = []
    for j in range(i - 2):
        s.append((j, i - j - 2))
    
    sr = set()
    for ss in s:
        sr.add(grundy[ss[0]] ^ grundy[ss[1]])

    grundy[i] = mex(sr)


if grundy[n] == 0: print(2)
else: print(1)
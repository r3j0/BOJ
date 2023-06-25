import sys
input = sys.stdin.readline

def checker(maps, m):
    S = [set() for _ in range((m**2)*2)]
    for i in range(m**2):
        for j in range(m**2):
            S[i].add(maps[i][j])
            S[m**2+j].add(maps[i][j])
    
    for i in range((m**2)*2):
        if len(S[i]) != m**2 or min(S[i]) != 1 or max(S[i]) != m**2:
            return 0
    
    for i in range(m):
        for j in range(m):
            S = set()
            for bi in range(m):
                for bj in range(m):
                    S.add(maps[i*m+bi][j*m+bj])
            
            if len(S) != m**2 or min(S) != 1 or max(S) != m**2:
                return 0
    return 1

t = int(input().rstrip())
for i in range(t):
    n = int(input().rstrip())
    maps = [list(map(int, input().rstrip().split())) for _ in range(n**2)]

    if checker(maps, n) == 1:
        print('Case #%d: Yes'%(i+1))
    else:
        print('Case #%d: No'%(i+1))
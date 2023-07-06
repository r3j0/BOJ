import sys
input = sys.stdin.readline

test = int(input().rstrip())
for t in range(test):
    if t != 0: input().rstrip()
    maps = [list(map(int, input().rstrip().split())) for _ in range(9)]

    done = 0
    #Sero
    for i in range(9):
        S = set()
        for j in range(9):
            S.add(maps[i][j])
        
        if len(S) != 9:
            done = 1
            break

    #Garo
    if done == 0:
        for j in range(9):
            S = set()
            for i in range(9):
                S.add(maps[i][j])

            if len(S) != 9:
                done = 1
                break

        #Block
        if done == 0:
            for bi in range(3):
                for bj in range(3):
                    S = set()
                    for ai in range(3):
                        for aj in range(3):
                            S.add(maps[bi*3+ai][bj*3+aj])
                    
                    if len(S) != 9:
                        done = 1
                        break
                if done == 1: break
    
    if done == 0: print('Case %d: CORRECT'%(t+1))
    else: print('Case %d: INCORRECT'%(t+1))
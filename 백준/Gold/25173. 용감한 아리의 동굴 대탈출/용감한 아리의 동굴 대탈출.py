import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

ariHp, ariAtk, bossHp, bossAtk = map(int, input().split())

debug = 0

def solve():
    global n, m, maps, ariHp, ariAtk, bossHp, bossAtk
    
    # 1. 아리와 보스의 위치 구하기
    ariPos = []
    bossPos = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2: ariPos = [i, j]
            if maps[i][j] == 3: bossPos = [i, j]

    # 2. 아리와 보스의 방향 구하기
    ariDir = -1
    bossDir = -1
    
    # 방향 : 상, 우, 하, 좌 
    row = [-1, 0, 1, 0]
    col = [0, 1, 0, -1]

    for d in range(4):
        keyN = bossPos[0] + row[d]
        keyM = bossPos[1] + col[d]

        if keyN == ariPos[0] and keyM == ariPos[1]:
            ariDir = d
            bossDir = d
            break
    
    while True:
        # 3. 아리의 공격
        bossHp -= ariAtk
        if bossHp <= 0: return "VICTORY!"

        # 4. 아리의 이동
        goN = ariPos[0] + row[ariDir]
        goM = ariPos[1] + col[ariDir]

        if 0 <= goN < n and 0 <= goM < m and maps[goN][goM] != 1:
            ariPos[0] = goN; ariPos[1] = goM
        else:
            # 만약 진행 불가라면
            for d in range(4):
                ariHp -= 1
                if ariHp == 0: return "CAVELIFE..."
                ariDir = (ariDir + 1) % 4
                
                goN = ariPos[0] + row[ariDir]
                goM = ariPos[1] + col[ariDir]

                if 0 <= goN < n and 0 <= goM < m and maps[goN][goM] != 1 and ( not ( goN == bossPos[0] and goM == bossPos[1] ) ): 
                    ariPos[0] = goN
                    ariPos[1] = goM
                    break

        if debug: print("AriHp : ", ariHp)

        if debug:
            print()
            for i in range(n):
                for j in range(m):
                    if i == bossPos[0] and j == bossPos[1]: print('3', end=' ')
                    elif i == ariPos[0] and j == ariPos[1]: print('2', end=' ')
                    else: 
                        if maps[i][j] == 2 or maps[i][j] == 3: print('0', end=' ')
                        else: print(str(maps[i][j]), end=' ')
                print()
            print()

        # 5. 보스의 공격

        # 상, 우, 하, 좌 상한
        maxLine = [bossPos[0], bossPos[1], bossPos[0], bossPos[1]]
        
        goDir = bossDir
        nowGo = [bossPos[0], bossPos[1]]
        changeCnt = 0
        dist = 1
        find = 0
        if debug: print("Finding suksun ... ")

        while maxLine[0] >= 0 or maxLine[1] < m or maxLine[2] < n or maxLine[3] >= 0:
            # 석순 찾기
            for d in range(dist):
                nowGo[0] += row[goDir]
                nowGo[1] += col[goDir]

                if nowGo[0] < maxLine[0]: maxLine[0] = nowGo[0] # 상
                if nowGo[1] > maxLine[1]: maxLine[1] = nowGo[1] # 우
                if nowGo[0] > maxLine[2]: maxLine[2] = nowGo[0] # 하
                if nowGo[1] < maxLine[3]: maxLine[3] = nowGo[1] # 좌
                #print(maxLine)

                if 0 <= nowGo[0] < n and 0 <= nowGo[1] < m and maps[nowGo[0]][nowGo[1]] == 1:
                    find = 1
                    break

            if find == 1: break

            goDir = (goDir + 1) % 4
            changeCnt += 1
            if changeCnt == 2:
                changeCnt = 0
                dist += 1

        if find == 1:
            if debug: print("Atk : ", nowGo[0], nowGo[1])
            # 6. 확인 완료, 공격 시작
            queue = deque()
            queue.append([nowGo[0], nowGo[1]])
            monsterHp = bossAtk

            done = 0
            while queue and monsterHp > 0:
                #print(queue)
                size = len(queue)
                visitDict = {}

                for s in range(size):
                    y, x = queue.popleft()

                    if y == ariPos[0] and x == ariPos[1]:
                        done = 1
                        break

                    for d in range(4):
                        ny = y + row[d]
                        nx = x + col[d]

                        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 1 and ( not (ny == bossPos[0] and nx == bossPos[1])):
                            if visitDict.get(ny, -1) != -1 and visitDict[ny].get(nx, -1) != -1:
                                continue
                            
                            if visitDict.get(ny, -1) == -1: visitDict[ny] = {}
                            visitDict[ny][nx] = 1
                            queue.append([ny, nx])
                
                if done == 1: break

                monsterHp -= 1
            
            if done == 1:
                ariHp -= monsterHp
                if debug: print(monsterHp, "-> (", ariHp + monsterHp, " -> ", ariHp, " ) ")

                if ariHp <= 0: return "CAVELIFE..."

        # 7. 보스의 이동
        if ( not ( bossPos[0] + row[bossDir] == ariPos[0] and bossPos[1] + col[bossDir] == ariPos[1] ) ):
            bossPos[0] += row[bossDir]
            bossPos[1] += col[bossDir]

        if bossDir != ariDir: bossDir = ariDir

print(solve())
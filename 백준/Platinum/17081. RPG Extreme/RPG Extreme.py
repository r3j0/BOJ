# 게임판 : N X M

# 게임판 요소 설명
# ( . ) : 빈 칸
# ( @ ) : 주인공 시작 지점
# ( # ) : 막힌 칸
# ( B ) : 아이템 상자, 먹으면 빈 칸
# 아이템 상자는 장비 중 한 가지
# 무기 ( W ), 갑옷 ( A ), 장신구 ( O )
# -> 아이템을 얻은 경우, 얻은 장비로 교체
# 장신구는 1. 칸이 남고
#         2. 동일 효과 장신구 착용 않을 때
# ( ^ ) : 가시 함정. 5 데미지, 안 사라짐
#         못 움직이면 또 밟은 거임
# ( & ) : 몬스터 -> 이름, 공격력, 방어력, 체력, 경험치 값
#         몬스터 전투 -> 주인공 선공, 공격 시 max(1, 내 공격력 - 상대의 방어력) 데미지
# ( M ) : 보스 몬스터

# 정보 설명
# 체력 ,공격력, 방어력 : 정수 표시 ( 초기 체력 20 공격력 2 방어력 2 )
# 경험치 : 처음엔 레벨 1. 레벨 업 조건 -> 5 x ( 현재 레벨 )
# 레벨업 시 남은 경험치는 버림. 최대 HP 5, 공 방 2 씩 더지고 HP 회복
# 무기 : 한 개 착용 가능. 주인공 공격력에 더해진다.
#   (주인공 공격력 + 무기 공격력) * 공격력 상승 효과
# 방어구 : 한 개 착용 가능. 주인공 방어력에 더해진다.
# 장신구 : 최대 4개까지 착용 가능. 동일 효과는 하나만 착용 가능
# - 장신구 효과
#   HP Regeneration (HR) : 전투 승리 시 체력 3 회복 ( 최대 체력까지 )
#   Reincarnation (RE) : 주인공 사망 시 장신구 소멸, 최대 체력으로 부활 시키고 시작 위치로
#                        정보는 변함 없지만 전투 중이었던 몬스터도 체력 최대 회복
#   Courage (CO) : 모든 전투 첫 번째 공격에서 주인공 공격력 (무기까지 더해진) 게 두 배
#                   -> max(1, 공격력x2 - 방어력)
#   Experience (EX) : 얻는 경험치 1.2배. 소수점 아래 버림
#   Dexterity (DX) : 가시 함정에 입는 데미지 1 고정. Courag와 함께 착용하면 공격력 세 배
#   Hunter (HU) : 보스 몬스터와 전투 돌입 시 최대회복, 보스몬스터 첫 공격 데미지 무시
#   Cursed (CU) : 걍 자리 차지

# 게임 룰 설명
# 주인공 : 상하 좌우 한 칸 이동, L, R, U, D로 이동이 주어짐. 못 움직이면 이동 X

# 게임 종료 조건 : 보스 몬스터 처치, 주인공 사망, 모든 커맨드 마쳤을 때
# - 보스 몬스터 처치 시 경험치 획득하고 레벨 업 장신구 효과 다 진행하고 게임 끝
# - 입력 다 안 끝났는데 게임 끝나면 남은 입력 무시

# 게임 종료 시 결과 출력
# - 현재 맵 상태
# - 주인공 : @ ( 함정이 있든 뭐가 있든 @로 출력 ) 사망 시 사라짐. 패배하면 출력 X
# - 빈 칸 : .
# - 벽 : #

# Passed Turns : T ( 진행된 턴 수. 게임은 0턴에서 시작한다. 첫 이동 하면 1턴 )
# LV : <현재 레벨>
# HP : <현재 남은 체력>/<최대 체력>
# ATT : <주공>+<무공>
# DEF : <주방>+<방방>
# EXP : <현재 경험치>/<요구 경험치>

# YOU WIN! ( 보스 몬스터 처치 )
# YOU HAVE BEEN KILLED BY <몬스터 이름 or SPIKE TRAP> 
# Press any key to continue. ( 입력 끝 )

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]

monster = {}
monster_num = 0

chest = {}
chest_num = 0

maps_monster_id = [[-1 for _ in range(m)] for _ in range(n)] 
maps_chest_id = [[-1 for _ in range(m)] for _ in range(n)]

startPos = []

for i in range(n):
    for j in range(m):
        now = maps[i][j]

        if now == '&' or now == 'M': 
            maps_monster_id[i][j] = monster_num
            monster_num += 1
        elif now == 'B': 
            maps_chest_id[i][j] = chest_num
            chest_num += 1
        elif now == '@':
            maps[i][j] = '.'
            startPos = [i, j]

moveOrder = list(input().rstrip())
movePos = {'U':[-1, 0], 'D':[1, 0], 'L':[0, -1], 'R':[0, 1]}

for i in range(monster_num):
    r, c, s, w, a, h, e = input().rstrip().split()
    now_id = maps_monster_id[int(r) - 1][int(c) - 1]
    monster[now_id] = {'Name':s, 'HP':int(h), 'ATK':int(w), 'DEF':int(a), 'MHP':int(h), 'EXP': int(e)}

for i in range(chest_num):
    r, c, t, s = input().rstrip().split()
    now_id = maps_chest_id[int(r) - 1][int(c) - 1]
    chest[now_id] = {'Type':t, 'Value':s}
    if t == 'W' or t == 'A':
        chest[now_id]['Value'] = int(s)

nowPlayerPos = [startPos[0], startPos[1]]
player = {'HP':20, 'MHP':20, 'ATK':2, 'DEF':2, 'LV':1, 'EXP':0, 'WN':-1, 'AN':-1, 'ON':[-1,-1,-1,-1]}
turns = 0
prev_monster_id = -1
result = 2
result_s = ['YOU WIN!', 'YOU HAVE BEEN KILLED BY ', 'Press any key to continue.']

def isSetted(effect, lis):
    global chest
    for l in lis:
        if l != -1 and chest[l]['Value'] == effect: return 1
    return 0

def openChest(y, x):
    global chest
    global maps_chest_id
    global player
    now_id = maps_chest_id[y][x]

    t = chest[now_id]['Type']
    if t == 'W': 
        player['WN'] = now_id
    elif t == 'A': 
        player['AN'] = now_id
    elif t == 'O': 
        if not isSetted(chest[now_id]['Value'], player['ON']):
            for k in range(4):
                if player['ON'][k] == -1:
                    player['ON'][k] = now_id
                    break

def isPlayerDied():
    global player
    global nowPlayerPos
    global prev_monster_id
    global result
    global maps 
    if player['HP'] <= 0:
        player['HP'] = 0
    else:
        return 0

    if isSetted('RE', player['ON']):
        player['HP'] = player['MHP']
        for k in range(4):
            if player['ON'][k] != -1 and chest[player['ON'][k]]['Value'] == 'RE':
                player['ON'][k] = -1
                break
        
        nowPlayerPos[0] = startPos[0]
        nowPlayerPos[1] = startPos[1]
        prev_monster_id = -1
        return 0
    else:
        result = 1
        return 1

def playerAtkCalc(battleturn):
    global player
    global chest
    now_atk = player['ATK']

    if player['WN'] != -1:
        now_atk += chest[player['WN']]['Value']
    
    if battleturn == 0 and isSetted('CO', player['ON']):
        if isSetted('DX', player['ON']): now_atk *= 3
        else: now_atk *= 2

    return now_atk
def playerDefCalc():
    global player
    global chest
    now_def = player['DEF']

    if player['AN'] != -1:
        now_def += chest[player['AN']]['Value']
    
    return now_def

def levelUp():
    global player
    player['MHP'] += 5
    player['HP'] = player['MHP']
    player['ATK'] += 2
    player['DEF'] += 2
    player['EXP'] = 0
    player['LV'] += 1

def enterBattle(monster_id):
    global monster
    global player
    global nowPlayerPos
    global maps
    now_turn = 0 # 0 : Player / 1 : Monster
    sum_turn = 0

    while True:
        if now_turn == 0: # Player Turn
            player_atk = playerAtkCalc(sum_turn) # 'CO', 'DX'
            monster[monster_id]['HP'] -= max(1, player_atk - monster[monster_id]['DEF'])

            if monster[monster_id]['HP'] <= 0:
                maps[nowPlayerPos[0]][nowPlayerPos[1]] = '.'
                gain_exp = monster[monster_id]['EXP']
                if isSetted('EX', player['ON']): 
                    gain_exp = int(gain_exp * 1.2)
                if isSetted('HR', player['ON']):
                    player['HP'] = min(player['MHP'], player['HP'] + 3)
                player['EXP'] += gain_exp
                if player['EXP'] >= player['LV']*5: levelUp()
                return

        else: # Monster Turn
            player_def = playerDefCalc() # 'HU'
            if sum_turn == 0 and isSetted('HU', player['ON']) and maps[nowPlayerPos[0]][nowPlayerPos[1]] == 'M': 
                player['HP'] -= 0
            else:
                player['HP'] -= max(1, monster[monster_id]['ATK'] - player_def)

            if player['HP'] <= 0:
                monster[monster_id]['HP'] = monster[monster_id]['MHP']
                return
            
            if sum_turn == 0: sum_turn = 1
        now_turn = (now_turn + 1) % 2

def printGame():
    global maps
    global turns
    global player
    global nowPlayerPos
    global result
    global chest

    for i in range(n):
        for j in range(m):
            if nowPlayerPos[0] == i and nowPlayerPos[1] == j and result != 1:
                print('@', end='')
            else:
                print(maps[i][j], end='')
        print()
    print("Passed Turns :", turns)
    print("LV :", player['LV'])
    print("HP : %d/%d"%(player['HP'], player['MHP']))
    w_atk = chest[player['WN']]['Value'] if player['WN'] != -1 else 0
    a_def = chest[player['AN']]['Value'] if player['AN'] != -1 else 0
    print("ATT : %d+%d"%(player['ATK'], w_atk))
    print("DEF : %d+%d"%(player['DEF'], a_def))
    print("EXP : %d/%d"%(player['EXP'], player['LV']*5))

for mos in moveOrder:
    goPos = movePos[mos]
    
    turns += 1
    #print(turns)
    if 0 <= nowPlayerPos[0] + goPos[0] < n and 0 <= nowPlayerPos[1] + goPos[1] < m and maps[nowPlayerPos[0] + goPos[0]][nowPlayerPos[1] + goPos[1]] != '#':
        nowPlayerPos[0] += goPos[0]
        nowPlayerPos[1] += goPos[1]

    # Act
    if maps[nowPlayerPos[0]][nowPlayerPos[1]] == '&':
        prev_monster_id = maps_monster_id[nowPlayerPos[0]][nowPlayerPos[1]]
        enterBattle(maps_monster_id[nowPlayerPos[0]][nowPlayerPos[1]])

        if isPlayerDied(): 
            break

    elif maps[nowPlayerPos[0]][nowPlayerPos[1]] == 'M':
        boss_y = nowPlayerPos[0]
        boss_x = nowPlayerPos[1]
        prev_monster_id = maps_monster_id[nowPlayerPos[0]][nowPlayerPos[1]]
        if isSetted('HU', player['ON']): player['HP'] = player['MHP']
        enterBattle(maps_monster_id[nowPlayerPos[0]][nowPlayerPos[1]])

        if isPlayerDied(): 
            break
        else:
            if maps[boss_y][boss_x] == '.':
                result = 0
                break

    elif maps[nowPlayerPos[0]][nowPlayerPos[1]] == 'B':
        openChest(nowPlayerPos[0], nowPlayerPos[1])
        maps[nowPlayerPos[0]][nowPlayerPos[1]] = '.'

    elif maps[nowPlayerPos[0]][nowPlayerPos[1]] == '^':
        if isSetted('DX', player['ON']): player['HP'] -= 1
        else: player['HP'] -= 5
        prev_monster_id = -1
        if isPlayerDied(): break

    #printGame()

printGame()
if result == 1:
    killed_by = ""
    if prev_monster_id == -1: killed_by = "SPIKE TRAP"
    else: killed_by = monster[prev_monster_id]['Name']
    print(result_s[result] + killed_by + "..")
else:
    print(result_s[result])
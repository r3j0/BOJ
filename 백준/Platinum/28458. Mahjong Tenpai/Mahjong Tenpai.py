import sys
input = sys.stdin.readline

board = {
    "1s":0, "2s":0, "3s":0, "4s":0, "5s":0, "6s":0, "7s":0, "8s":0, "9s":0, 
    "1t":0, "2t":0, "3t":0, "4t":0, "5t":0, "6t":0, "7t":0, "8t":0, "9t":0, 
    "1m":0, "2m":0, "3m":0, "4m":0, "5m":0, "6m":0, "7m":0, "8m":0, "9m":0, 

    "e":0, "w":0, "s":0, "n":0, "h":0, "b":0, "j":0
}
arr = list(input().rstrip().split())
for a in arr:
    board[a] += 1

first_board = {
    "1s":0, "2s":0, "3s":0, "4s":0, "5s":0, "6s":0, "7s":0, "8s":0, "9s":0, 
    "1t":0, "2t":0, "3t":0, "4t":0, "5t":0, "6t":0, "7t":0, "8t":0, "9t":0, 
    "1m":0, "2m":0, "3m":0, "4m":0, "5m":0, "6m":0, "7m":0, "8m":0, "9m":0, 

    "e":0, "w":0, "s":0, "n":0, "h":0, "b":0, "j":0
}
for k, v in board.items():
    first_board[k] = v

# 필요한 패
need = {}

# 1. 치또이츠
# 2 2 2 2 2 2 2 여야 함.
# 2 2 2 2 2 3 (1) -> X ( 똑같은 패 4 장 )
# 2 2 2 2 2 2 1 -> O
# 1개 가진 패 종류가 1개, 2개 가진 패 종류가 6개면 치또이츠

one_pai = []
two_pai = 0
for a in board.keys():
    if board[a] == 1: 
        one_pai.append(a)
    elif board[a] == 2:
        two_pai += 1

if len(one_pai) == 1 and two_pai == 6 and first_board[one_pai[0]] != 4:
    need[one_pai[0]] = 1

# 2. 국사무쌍
# 1s, 9s, 1m, 9m, 1t, 9t, e, w, s, n, h, b, j
# 이 종류의 패를 전부 다 세서 
# 1개 종류가 13개다 -> 이 13개 전부 need
# 1개 종류가 11개고 2개 종류가 1개다 -> 남은 1개가 need

guksamussang = ['1s', '9s', '1m', '9m', '1t', '9t', 'e', 'w', 's', 'n', 'h', 'b', 'j']
zero_pai = []
one_pai = 0
two_pai = 0

for a in guksamussang:
    if board[a] == 0: zero_pai.append(a)
    elif board[a] == 1: one_pai += 1
    elif board[a] == 2: two_pai += 1

if one_pai == 13:
    for a in guksamussang:
        need[a] = 1
elif one_pai == 11 and two_pai == 1:
    need[zero_pai[0]] = 1

# 머리 1개, 몸통 4개
# 머리 1개가 없거나 ( 패 1개 남아서 ) 몸통 4개
# 몸통 중 1개가 없거나 ( 머리 2개 / 머리 1개 몸통 유실 1개 ) 몸통 3개

# 몸통 백트래킹으로 찾고 -> 남은 장수
# 1장 (슌쯔, 커쯔로 가져감) -> 그 1장 가져갈 수 있으면 그게 need ( 나머지는 백트래킹으로 찾기 가능 )
# 4장 -> 같은 거 있는걸 머리로 가져가고, 나머지 2개가 슌쯔 되길 빌거나 혹은 2개 다 머리

# 몸통 슌쯔 발견
# 2 3 3 4 -> 3
# 1 2 3 3 -> 3
# 2 2 3 4 -> 2
# 1 5 6 7 -> 1
# 1 2 3 4 -> 1 or 4
# 몸통 커쯔 발견
# 1 2 2 2 -> 1
# 2 2 2 2 -> 2 못함. 4장밖에 없으니까 -> 내가 4개를 가져갔는지 체크하기
# 2 2 2 3 -> 3
# 2 2 2 5 -> 5

# 몸통 발견 못함 ( 머리 후보 2개일수도 )
# 머후2 1 1 9 9 -> 1 or 9
# 머후1 1 1 3 5 -> 4
# 머후1 1 2 4 4 -> 3
# 머후0 1 3 5 6 -> 이러면 답이 없음

# 조합 만들기
def makeJohab(b):
    lis = []
    # 슌쯔
    for i in range(1, 8):
        if b[str(i)+'s'] > 0 and b[str(i+1)+'s'] > 0 and b[str(i+2)+'s'] > 0:
            lis.append(str(i)+'s,'+str(i+1)+'s,'+str(i+2)+'s')
        if b[str(i)+'t'] > 0 and b[str(i+1)+'t'] > 0 and b[str(i+2)+'t'] > 0:
            lis.append(str(i)+'t,'+str(i+1)+'t,'+str(i+2)+'t')
        if b[str(i)+'m'] > 0 and b[str(i+1)+'m'] > 0 and b[str(i+2)+'m'] > 0:
            lis.append(str(i)+'m,'+str(i+1)+'m,'+str(i+2)+'m')
    
    # 커쯔
    for k in b.keys():
        if b[k] >= 3: 
            lis.append("%s,%s,%s"%(k,k,k))
    
    # 머리
    for k in b.keys():
        if b[k] >= 2: 
            lis.append("%s,%s"%(k,k))

    return lis

# 백트래킹으로 조합들 하나씩 세기
def backtracking(can_johab, available_pai, muri):
    #print(can_johab)
    if len(can_johab) == 0 or (muri == 1 and len(can_johab) <= 1):
        #print('Comp')
        # 1개 남았을 때
        if sum(list(available_pai.values())) == 1:
            go = ''
            for ak in available_pai.keys():
                if available_pai[ak] == 1:
                    go = ak
                    break
            if first_board[go] != 4: 
                #print('Need', go)
                """ for k, v in available_pai.items():
                    if v > 0: print(k, v, end=' ')
                print()
                print() """
                need[go] = 1
        elif sum(list(available_pai.values())) == 2:
            """ for k, v in available_pai.items():
                if v > 0: print(k, v, end=' ')
            print()
            print() """
        
            # 남은 걸로 슌쯔를 만들기
            one_pai = []
            for k, v in available_pai.items():
                if v == 1:
                    one_pai.append(k)
            
            if len(one_pai) == 2 and len(one_pai[0]) == 2 and len(one_pai[1]) == 2 and one_pai[0][1] == one_pai[1][1]:
                if abs(int(one_pai[0][0]) - int(one_pai[1][0])) == 1: # 양옆
                    first_num = (int(one_pai[0][0]) + int(one_pai[1][0]))//2
                    if first_num - 1 >= 1 and first_board[str(first_num-1) + one_pai[0][1]] != 4: 
                        need[str(first_num-1) + one_pai[0][1]] = 1
                    if first_num + 2 <= 9 and first_board[str(first_num+2) + one_pai[0][1]] != 4: 
                        need[str(first_num+2) + one_pai[0][1]] = 1
                elif abs(int(one_pai[0][0]) - int(one_pai[1][0])) == 2 and first_board[str((int(one_pai[0][0]) + int(one_pai[1][0]))//2) + one_pai[0][1]] != 4: # 중간
                    need[str((int(one_pai[0][0]) + int(one_pai[1][0]))//2) + one_pai[0][1]] = 1

            # 남은 걸로 커쯔를 만들기
            for k, v in available_pai.items():
                if v == 2 and first_board[k] != 4: 
                    need[k] = 1
                    break
        elif sum(list(available_pai.values())) == 4: # 4
            one_pai = []
            two_pai = []
            for ak in available_pai.keys():
                if available_pai[ak] == 1: one_pai.append(ak)
                elif available_pai[ak] == 2: two_pai.append(ak)
            
            #print(one_pai, two_pai)
            if len(two_pai) == 2:
                if first_board[two_pai[0]] != 4: 
                    need[two_pai[0]] = 1
                    #print('Need', two_pai[0])
                if first_board[two_pai[1]] != 4: 
                    need[two_pai[1]] = 1
                    #print('Need', two_pai[1])
            elif len(two_pai) == 1 and len(one_pai) == 2 and '1' <= one_pai[0][0] <= '9' and '1' <= one_pai[1][0] <= '9' and one_pai[0][1] == one_pai[1][1] :
                a, b = min(int(one_pai[0][0]), int(one_pai[1][0])), max(int(one_pai[0][0]), int(one_pai[1][0]))
                if b - a == 1:
                    # b + 1
                    if b + 1 <= 9 and first_board[str(b+1)+one_pai[0][1]] != 4:
                        need[str(b+1)+one_pai[0][1]] = 1
                        #print('Need', str(b+1)+one_pai[0][1])
                    # a - 1
                    if a - 1 >= 1 and first_board[str(a-1)+one_pai[0][1]] != 4:
                        need[str(a-1)+one_pai[0][1]] = 1
                        #print('Need', str(a-1)+one_pai[0][1])
                elif b - a == 2:
                    # b - 1
                    if first_board[str(b-1)+one_pai[0][1]] != 4:
                        need[str(b-1)+one_pai[0][1]] = 1
                        #print('Need', str(b-1)+one_pai[0][1])

        return
    
    # 조합으로 반복문
    for nck in can_johab:
        npai = list(nck.split(','))
        if len(npai) == 2 and muri == 1: continue
        for npai_idx in npai:
            available_pai[npai_idx] -= 1
        if len(npai) == 2: muri = 1
        backtracking(makeJohab(available_pai), available_pai, muri)
        if len(npai) == 2: muri = 0
        for npai_idx in npai:
            available_pai[npai_idx] += 1

backtracking(makeJohab(board), {k:v for k, v in board.items()}, 0)

# 종국

if len(need) > 0: 
    print('tenpai')
    print(len(need))
    result = list(need.keys())
    result.sort()
    print(' '.join(result))
else: print('no tenpai')
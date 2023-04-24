import sys
input = sys.stdin.readline

maps = [list(input().rstrip()) for _ in range(3)]

solo_winner = {}
solo = 0
# 1. Solo Row
for i in range(3):
    dic = {}
    for j in range(3):
        if dic.get(maps[i][j], -1) == -1:
            dic[maps[i][j]] = 1
        else:
            dic[maps[i][j]] += 1
    
    if len(dic) == 1 and solo_winner.get(list(dic.keys())[0], -1) == -1: 
        solo += 1
        solo_winner[list(dic.keys())[0]] = 1

# 2. Solo Column
for i in range(3):
    dic = {}
    for j in range(3):
        if dic.get(maps[j][i], -1) == -1:
            dic[maps[j][i]] = 1
        else:
            dic[maps[j][i]] += 1
    
    if len(dic) == 1 and solo_winner.get(list(dic.keys())[0], -1) == -1: 
        solo += 1
        solo_winner[list(dic.keys())[0]] = 1

# 3. Solo Diag
dic = {}
for i in range(3):
    if dic.get(maps[i][i], -1) == -1:
        dic[maps[i][i]] = 1
    else:
        dic[maps[i][i]] += 1

if len(dic) == 1 and solo_winner.get(list(dic.keys())[0], -1) == -1: 
    solo += 1
    solo_winner[list(dic.keys())[0]] = 1

dic = {}
for i in range(3):
    if dic.get(maps[2-i][i], -1) == -1:
        dic[maps[2-i][i]] = 1
    else:
        dic[maps[2-i][i]] += 1

if len(dic) == 1 and solo_winner.get(list(dic.keys())[0], -1) == -1: 
    solo += 1
    solo_winner[list(dic.keys())[0]] = 1

print(solo)

duo_winner = {}
duo = 0
# 1. Duo Row
for i in range(3):
    dic = {}
    for j in range(3):
        if dic.get(maps[i][j], -1) == -1:
            dic[maps[i][j]] = 1
        else:
            dic[maps[i][j]] += 1
    
    if len(dic) == 2 and duo_winner.get(sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1], -1) == -1: 
        duo += 1
        duo_winner[sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1]] = 1

# 2. Duo Column
for i in range(3):
    dic = {}
    for j in range(3):
        if dic.get(maps[j][i], -1) == -1:
            dic[maps[j][i]] = 1
        else:
            dic[maps[j][i]] += 1
    
    if len(dic) == 2 and duo_winner.get(sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1], -1) == -1:
        duo += 1
        duo_winner[sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1]] = 1

# 3. Duo Diag
dic = {}
for i in range(3):
    if dic.get(maps[i][i], -1) == -1:
        dic[maps[i][i]] = 1
    else:
        dic[maps[i][i]] += 1

if len(dic) == 2 and duo_winner.get(sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1], -1) == -1: 
    duo += 1
    duo_winner[sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1]] = 1

dic = {}
for i in range(3):
    if dic.get(maps[2-i][i], -1) == -1:
        dic[maps[2-i][i]] = 1
    else:
        dic[maps[2-i][i]] += 1

if len(dic) == 2 and duo_winner.get(sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1], -1) == -1: 
    duo += 1
    duo_winner[sorted(list(dic.keys()))[0] + "_" + sorted(list(dic.keys()))[1]] = 1

print(duo)
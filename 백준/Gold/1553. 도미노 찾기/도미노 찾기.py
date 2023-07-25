import sys
input = sys.stdin.readline

maps = [list(input().rstrip()) for _ in range(8)]
for i in range(8):
    for j in range(7):
        maps[i][j] = int(maps[i][j])

result = 0
def backtracking(now_maps, now_available):
    global maps
    global result

    if len(now_available) == 0:
        result += 1
        return
    
    start = []
    for i in range(8):
        for j in range(7):
            if now_maps[i][j] == -1:
                start = [i, j]
                break
        if len(start) != 0:
            break
    
    now = maps[start[0]][start[1]]
    # Right
    if start[0]+1 < 8 and now_maps[start[0]+1][start[1]] == -1:
        go = maps[start[0]+1][start[1]]
        if now == 0:
            if go == 0 and '00' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 0
                del now_available['00']
                backtracking(now_maps, now_available)
                now_available['00'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '01' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 1
                del now_available['01']
                backtracking(now_maps, now_available)
                now_available['01'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '02' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 2
                del now_available['02']
                backtracking(now_maps, now_available)
                now_available['02'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '03' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 3
                del now_available['03']
                backtracking(now_maps, now_available)
                now_available['03'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '04' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 4
                del now_available['04']
                backtracking(now_maps, now_available)
                now_available['04'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '05' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 5
                del now_available['05']
                backtracking(now_maps, now_available)
                now_available['05'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '06' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]+1][start[1]] = 6
                del now_available['06']
                backtracking(now_maps, now_available)
                now_available['06'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
        elif now == 1:
            if go == 0 and '01' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 0
                del now_available['01']
                backtracking(now_maps, now_available)
                now_available['01'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '11' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 1
                del now_available['11']
                backtracking(now_maps, now_available)
                now_available['11'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '12' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 2
                del now_available['12']
                backtracking(now_maps, now_available)
                now_available['12'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '13' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 3
                del now_available['13']
                backtracking(now_maps, now_available)
                now_available['13'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '14' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 4
                del now_available['14']
                backtracking(now_maps, now_available)
                now_available['14'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '15' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 5
                del now_available['15']
                backtracking(now_maps, now_available)
                now_available['15'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '16' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]+1][start[1]] = 6
                del now_available['16']
                backtracking(now_maps, now_available)
                now_available['16'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
        elif now == 2:
            if go == 0 and '02' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 0
                del now_available['02']
                backtracking(now_maps, now_available)
                now_available['02'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '12' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 1
                del now_available['12']
                backtracking(now_maps, now_available)
                now_available['12'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '22' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 2
                del now_available['22']
                backtracking(now_maps, now_available)
                now_available['22'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '23' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 3
                del now_available['23']
                backtracking(now_maps, now_available)
                now_available['23'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '24' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 4
                del now_available['24']
                backtracking(now_maps, now_available)
                now_available['24'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '25' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 5
                del now_available['25']
                backtracking(now_maps, now_available)
                now_available['25'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '26' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]+1][start[1]] = 6
                del now_available['26']
                backtracking(now_maps, now_available)
                now_available['26'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
        elif now == 3:
            if go == 0 and '03' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 0
                del now_available['03']
                backtracking(now_maps, now_available)
                now_available['03'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '13' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 1
                del now_available['13']
                backtracking(now_maps, now_available)
                now_available['13'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '23' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 2
                del now_available['23']
                backtracking(now_maps, now_available)
                now_available['23'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '33' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 3
                del now_available['33']
                backtracking(now_maps, now_available)
                now_available['33'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '34' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 4
                del now_available['34']
                backtracking(now_maps, now_available)
                now_available['34'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '35' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 5
                del now_available['35']
                backtracking(now_maps, now_available)
                now_available['35'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '36' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]+1][start[1]] = 6
                del now_available['36']
                backtracking(now_maps, now_available)
                now_available['36'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
        elif now == 4:
            if go == 0 and '04' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 0
                del now_available['04']
                backtracking(now_maps, now_available)
                now_available['04'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '14' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 1
                del now_available['14']
                backtracking(now_maps, now_available)
                now_available['14'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '24' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 2
                del now_available['24']
                backtracking(now_maps, now_available)
                now_available['24'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '34' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 3
                del now_available['34']
                backtracking(now_maps, now_available)
                now_available['34'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '44' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 4
                del now_available['44']
                backtracking(now_maps, now_available)
                now_available['44'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '45' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 5
                del now_available['45']
                backtracking(now_maps, now_available)
                now_available['45'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '46' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]+1][start[1]] = 6
                del now_available['46']
                backtracking(now_maps, now_available)
                now_available['46'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
        elif now == 5:
            if go == 0 and '05' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 0
                del now_available['05']
                backtracking(now_maps, now_available)
                now_available['05'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '15' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 1
                del now_available['15']
                backtracking(now_maps, now_available)
                now_available['15'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '25' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 2
                del now_available['25']
                backtracking(now_maps, now_available)
                now_available['25'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '35' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 3
                del now_available['35']
                backtracking(now_maps, now_available)
                now_available['35'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '45' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 4
                del now_available['45']
                backtracking(now_maps, now_available)
                now_available['45'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '55' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 5
                del now_available['55']
                backtracking(now_maps, now_available)
                now_available['55'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '56' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]+1][start[1]] = 6
                del now_available['56']
                backtracking(now_maps, now_available)
                now_available['56'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
        elif now == 6:
            if go == 0 and '06' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 0
                del now_available['06']
                backtracking(now_maps, now_available)
                now_available['06'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 1 and '16' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 1
                del now_available['16']
                backtracking(now_maps, now_available)
                now_available['16'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 2 and '26' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 2
                del now_available['26']
                backtracking(now_maps, now_available)
                now_available['26'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 3 and '36' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 3
                del now_available['36']
                backtracking(now_maps, now_available)
                now_available['36'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 4 and '46' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 4
                del now_available['46']
                backtracking(now_maps, now_available)
                now_available['46'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 5 and '56' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 5
                del now_available['56']
                backtracking(now_maps, now_available)
                now_available['56'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
            elif go == 6 and '66' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]+1][start[1]] = 6
                del now_available['66']
                backtracking(now_maps, now_available)
                now_available['66'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]+1][start[1]] = -1
    # Right
    if start[1]+1 < 7 and now_maps[start[0]][start[1]+1] == -1:
        go = maps[start[0]][start[1]+1]
        if now == 0:
            if go == 0 and '00' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 0
                del now_available['00']
                backtracking(now_maps, now_available)
                now_available['00'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '01' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 1
                del now_available['01']
                backtracking(now_maps, now_available)
                now_available['01'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '02' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 2
                del now_available['02']
                backtracking(now_maps, now_available)
                now_available['02'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '03' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 3
                del now_available['03']
                backtracking(now_maps, now_available)
                now_available['03'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '04' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 4
                del now_available['04']
                backtracking(now_maps, now_available)
                now_available['04'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '05' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 5
                del now_available['05']
                backtracking(now_maps, now_available)
                now_available['05'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '06' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 0
                now_maps[start[0]][start[1]+1] = 6
                del now_available['06']
                backtracking(now_maps, now_available)
                now_available['06'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
        elif now == 1:
            if go == 0 and '01' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 0
                del now_available['01']
                backtracking(now_maps, now_available)
                now_available['01'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '11' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 1
                del now_available['11']
                backtracking(now_maps, now_available)
                now_available['11'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '12' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 2
                del now_available['12']
                backtracking(now_maps, now_available)
                now_available['12'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '13' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 3
                del now_available['13']
                backtracking(now_maps, now_available)
                now_available['13'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '14' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 4
                del now_available['14']
                backtracking(now_maps, now_available)
                now_available['14'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '15' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 5
                del now_available['15']
                backtracking(now_maps, now_available)
                now_available['15'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '16' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 1
                now_maps[start[0]][start[1]+1] = 6
                del now_available['16']
                backtracking(now_maps, now_available)
                now_available['16'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
        elif now == 2:
            if go == 0 and '02' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 0
                del now_available['02']
                backtracking(now_maps, now_available)
                now_available['02'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '12' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 1
                del now_available['12']
                backtracking(now_maps, now_available)
                now_available['12'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '22' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 2
                del now_available['22']
                backtracking(now_maps, now_available)
                now_available['22'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '23' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 3
                del now_available['23']
                backtracking(now_maps, now_available)
                now_available['23'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '24' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 4
                del now_available['24']
                backtracking(now_maps, now_available)
                now_available['24'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '25' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 5
                del now_available['25']
                backtracking(now_maps, now_available)
                now_available['25'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '26' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 2
                now_maps[start[0]][start[1]+1] = 6
                del now_available['26']
                backtracking(now_maps, now_available)
                now_available['26'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
        elif now == 3:
            if go == 0 and '03' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 0
                del now_available['03']
                backtracking(now_maps, now_available)
                now_available['03'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '13' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 1
                del now_available['13']
                backtracking(now_maps, now_available)
                now_available['13'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '23' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 2
                del now_available['23']
                backtracking(now_maps, now_available)
                now_available['23'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '33' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 3
                del now_available['33']
                backtracking(now_maps, now_available)
                now_available['33'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '34' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 4
                del now_available['34']
                backtracking(now_maps, now_available)
                now_available['34'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '35' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 5
                del now_available['35']
                backtracking(now_maps, now_available)
                now_available['35'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '36' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 3
                now_maps[start[0]][start[1]+1] = 6
                del now_available['36']
                backtracking(now_maps, now_available)
                now_available['36'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
        elif now == 4:
            if go == 0 and '04' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 0
                del now_available['04']
                backtracking(now_maps, now_available)
                now_available['04'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '14' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 1
                del now_available['14']
                backtracking(now_maps, now_available)
                now_available['14'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '24' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 2
                del now_available['24']
                backtracking(now_maps, now_available)
                now_available['24'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '34' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 3
                del now_available['34']
                backtracking(now_maps, now_available)
                now_available['34'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '44' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 4
                del now_available['44']
                backtracking(now_maps, now_available)
                now_available['44'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '45' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 5
                del now_available['45']
                backtracking(now_maps, now_available)
                now_available['45'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '46' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 4
                now_maps[start[0]][start[1]+1] = 6
                del now_available['46']
                backtracking(now_maps, now_available)
                now_available['46'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
        elif now == 5:
            if go == 0 and '05' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 0
                del now_available['05']
                backtracking(now_maps, now_available)
                now_available['05'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '15' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 1
                del now_available['15']
                backtracking(now_maps, now_available)
                now_available['15'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '25' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 2
                del now_available['25']
                backtracking(now_maps, now_available)
                now_available['25'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '35' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 3
                del now_available['35']
                backtracking(now_maps, now_available)
                now_available['35'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '45' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 4
                del now_available['45']
                backtracking(now_maps, now_available)
                now_available['45'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '55' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 5
                del now_available['55']
                backtracking(now_maps, now_available)
                now_available['55'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '56' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 5
                now_maps[start[0]][start[1]+1] = 6
                del now_available['56']
                backtracking(now_maps, now_available)
                now_available['56'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
        elif now == 6:
            if go == 0 and '06' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 0
                del now_available['06']
                backtracking(now_maps, now_available)
                now_available['06'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 1 and '16' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 1
                del now_available['16']
                backtracking(now_maps, now_available)
                now_available['16'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 2 and '26' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 2
                del now_available['26']
                backtracking(now_maps, now_available)
                now_available['26'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 3 and '36' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 3
                del now_available['36']
                backtracking(now_maps, now_available)
                now_available['36'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 4 and '46' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 4
                del now_available['46']
                backtracking(now_maps, now_available)
                now_available['46'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 5 and '56' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 5
                del now_available['56']
                backtracking(now_maps, now_available)
                now_available['56'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1
            elif go == 6 and '66' in list(now_available.keys()):
                now_maps[start[0]][start[1]] = 6
                now_maps[start[0]][start[1]+1] = 6
                del now_available['66']
                backtracking(now_maps, now_available)
                now_available['66'] = 0
                now_maps[start[0]][start[1]] = -1
                now_maps[start[0]][start[1]+1] = -1

backtracking([[-1 for _ in range(7)] for _ in range(8)], 
             {'00':0, '01':0, '02':0, '03':0, '04':0, '05':0,
              '06':0, '11':0, '12':0, '13':0, '14':0, '15':0,
              '16':0, '22':0, '23':0, '24':0, '25':0, '26':0,
              '33':0, '34':0, '35':0, '36':0, '44':0, '45':0,
              '46':0, '55':0, '56':0, '66':0})

print(result)
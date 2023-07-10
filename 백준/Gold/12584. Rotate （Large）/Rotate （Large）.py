import sys
input = sys.stdin.readline

t = int(input().rstrip())
for ti in range(t):
    n, k = map(int, input().rstrip().split())

    arr = [list(input().rstrip()) for _ in range(n)]
    maps = [['.' for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n-1, -1, -1):
            maps[j][(n-1)-i] = arr[i][j]
    
    result = [['.' for _ in range(n)] for _ in range(n)]

    for j in range(n):
        now = []
        for i in range(n-1, -1, -1):
            if maps[i][j] != '.': now.append(maps[i][j])

        idx = 0
        for i in range(n-1, -1, -1):
            if idx >= len(now): break
            result[i][j] = now[idx]
            idx += 1
    
    red_on = 0
    blue_on = 0

    for i in range(n):
        for j in range(n):
            if result[i][j] == 'R':
                leftup_rightdown = [0, 0]
                
                idx = 1
                while i - idx > 0 and j - idx > 0 and result[i-idx][j-idx] == 'R':
                    idx += 1
                    leftup_rightdown[0] += 1

                idx = 1
                while i + idx < n and j + idx < n and result[i+idx][j+idx] == 'R':
                    idx += 1
                    leftup_rightdown[1] += 1
                
                if sum(leftup_rightdown) + 1 >= k:
                    red_on = 1
                    continue

                leftdown_rightup = [0, 0]

                idx = 1
                while i + idx < n and j - idx > 0 and result[i+idx][j-idx] == 'R':
                    idx += 1
                    leftdown_rightup[0] += 1

                idx = 1
                while i - idx > 0 and j + idx < n and result[i-idx][j+idx] == 'R':
                    idx += 1
                    leftdown_rightup[1] += 1
                
                if sum(leftdown_rightup) + 1 >= k:
                    red_on = 1
                    continue

                left_right = [0, 0]

                idx = 1
                while j - idx > 0 and result[i][j-idx] == 'R':
                    idx += 1
                    left_right[0] += 1

                idx = 1
                while j + idx < n and result[i][j+idx] == 'R':
                    idx += 1
                    left_right[1] += 1
                
                if sum(left_right) + 1 >= k:
                    red_on = 1
                    continue

                up_down = [0, 0]

                idx = 1
                while i - idx > 0 and result[i-idx][j] == 'R':
                    idx += 1
                    up_down[0] += 1

                idx = 1
                while i + idx < n and result[i+idx][j] == 'R':
                    idx += 1
                    up_down[1] += 1

                if sum(up_down) + 1 >= k:
                    red_on = 1
                    continue

            elif result[i][j] == 'B':
                leftup_rightdown = [0, 0]
                
                idx = 1
                while i - idx > 0 and j - idx > 0 and result[i-idx][j-idx] == 'B':
                    idx += 1
                    leftup_rightdown[0] += 1

                idx = 1
                while i + idx < n and j + idx < n and result[i+idx][j+idx] == 'B':
                    idx += 1
                    leftup_rightdown[1] += 1
                
                if sum(leftup_rightdown) + 1 >= k:
                    blue_on = 1
                    continue

                leftdown_rightup = [0, 0]

                idx = 1
                while i + idx < n and j - idx > 0 and result[i+idx][j-idx] == 'B':
                    idx += 1
                    leftdown_rightup[0] += 1

                idx = 1
                while i - idx > 0 and j + idx < n and result[i-idx][j+idx] == 'B':
                    idx += 1
                    leftdown_rightup[1] += 1
                
                if sum(leftdown_rightup) + 1 >= k:
                    blue_on = 1
                    continue

                left_right = [0, 0]

                idx = 1
                while j - idx > 0 and result[i][j-idx] == 'B':
                    idx += 1
                    left_right[0] += 1

                idx = 1
                while j + idx < n and result[i][j+idx] == 'B':
                    idx += 1
                    left_right[1] += 1
                
                if sum(left_right) + 1 >= k:
                    blue_on = 1
                    continue

                up_down = [0, 0]

                idx = 1
                while i - idx > 0 and result[i-idx][j] == 'B':
                    idx += 1
                    up_down[0] += 1

                idx = 1
                while i + idx < n and result[i+idx][j] == 'B':
                    idx += 1
                    up_down[1] += 1

                if sum(up_down) + 1 >= k:
                    blue_on = 1
                    continue

    if red_on == 1 and blue_on == 1: print('Case #%d: Both'%(ti+1))
    elif red_on == 0 and blue_on == 0: print('Case #%d: Neither'%(ti+1))
    elif red_on == 1: print('Case #%d: Red'%(ti+1))
    else: print('Case #%d: Blue'%(ti+1))
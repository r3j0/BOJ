debug = 0

test = int(input())
for t in range(test):
    n, m = map(int, input().split())

    arr = [list(input()) for _ in range(n)]
    visit = [[0 for j in range(m)] for i in range(n)]

    outs = []
    # 1. Outside Check
    for i in range(n):
        if arr[i][0] != '*': outs.append([i, 0])
        if arr[i][m-1] != '*': outs.append([i, m-1])
    for j in range(m):
        if arr[0][j] != '*': outs.append([0, j])
        if arr[n-1][j] != '*': outs.append([n-1, j])

    keys = list(input())

    # 2. First Outside Go
    doors = {}

    stack1 = []
    stack2 = []
    stack_mode = 1

    row = [-1, 1, 0, 0]
    col = [0, 0, -1, 1]

    docs = 0

    for o in outs:
        stack1.append([o[0], o[1]])
        visit[o[0]][o[1]] = 1

    while True:
        if debug:
            if stack_mode == 1: print('s1 :', stack1)
            else: print('s2 :', stack2)


        size = 0
        if stack_mode == 1: size = len(stack1)
        else: size = len(stack2)

        if size == 0: break

        for s in range(size):
            y = 0; x = 0
            if stack_mode == 1:
                y = stack1[s][0]
                x = stack1[s][1]
            else:
                y = stack2[s][0]
                x = stack2[s][1]

            if 'a' <= arr[y][x] <= 'z':
                keys.append(arr[y][x])
                if debug: print(arr[y][x], 'get key')
                arr[y][x] = '.'

            elif 'A' <= arr[y][x] <= 'Z':
                if doors.get(arr[y][x], -1) == -1: doors[arr[y][x]] = [[y, x]]
                else: doors[arr[y][x]].append([y, x])
                continue
                
            elif arr[y][x] == '$':
                docs += 1
                arr[y][x] = '.'

            for d in range(4):
                ny = y + row[d]
                nx = x + col[d]

                if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and arr[ny][nx] != '*':
                    visit[ny][nx] = 1

                    if stack_mode == 1: stack2.append([ny, nx])
                    else: stack1.append([ny, nx])
        
        if stack_mode == 1:
            stack_mode = 2
            stack1 = []
        else:
            stack_mode = 1
            stack2 = []
    
    while True:
        stack1 = []
        stack2 = []
        stack_mode = 1

        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]

        go = 0

        if debug: 
            print('Next Keys >>')
            print(keys)
        if len(keys) != 0:
            for k in keys:
                if doors.get(k.upper(), -1) != -1:
                    if debug: print(k, 'Use')
                    for dk in doors[k.upper()]:
                        arr[dk[0]][dk[1]] = '.'
                        stack1.append([dk[0], dk[1]])
                        if debug: print('goto',dk)
                    del doors[k.upper()]
                    go = 1

        if go == 0: break
        
        while True:
            if debug:
                if stack_mode == 1: print('s1 :', stack1)
                else: print('s2 :', stack2)

            size = 0
            if stack_mode == 1: size = len(stack1)
            else: size = len(stack2)

            if size == 0: break

            for s in range(size):    
                y = 0; x = 0
                if stack_mode == 1:
                    y = stack1[s][0]
                    x = stack1[s][1]
                else:
                    y = stack2[s][0]
                    x = stack2[s][1]

                if 'a' <= arr[y][x] <= 'z':
                    keys.append(arr[y][x])
                    if debug: print(arr[y][x], 'get key')
                    arr[y][x] = '.'

                elif 'A' <= arr[y][x] <= 'Z':
                    if doors.get(arr[y][x], -1) == -1: doors[arr[y][x]] = [[y, x]]
                    else: doors[arr[y][x]].append([y, x])
                    continue
                    
                elif arr[y][x] == '$':
                    docs += 1
                    arr[y][x] = '.'

                for d in range(4):
                    ny = y + row[d]
                    nx = x + col[d]

                    if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and arr[ny][nx] != '*':
                        visit[ny][nx] = 1

                        if stack_mode == 1: stack2.append([ny, nx])
                        else: stack1.append([ny, nx])
            
            if stack_mode == 1:
                stack_mode = 2
                stack1 = []
            else:
                stack_mode = 1
                stack2 = []

    print(docs)
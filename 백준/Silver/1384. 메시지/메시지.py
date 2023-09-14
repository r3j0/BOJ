import sys
input = sys.stdin.readline

t = 1
while True:
    n = int(input().rstrip())
    if n == 0: break
    arr = [list(input().rstrip().split()) for _ in range(n)]

    print('Group %d'%t)
    go = 0
    for i in range(n):
        for j in range(1, n):
            if arr[i][j] == 'N':
                who = arr[i - j if i - j >= 0 else i - j + n][0]
                print("%s was nasty about %s"%(who, arr[i][0]))
                go = 1
    
    if go == 0:
        print('Nobody was nasty')
    t += 1
    print()
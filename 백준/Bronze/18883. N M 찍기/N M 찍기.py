n, m = map(int, input().rstrip().split())
cnt = 1
for i in range(n):
    for j in range(m):
        print(cnt, end='')
        cnt += 1
        
        if j != m - 1: print(' ', end='')
    print()
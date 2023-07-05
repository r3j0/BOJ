import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
if k < (m+(n-1)): print('NO')
else:
    print('YES')

    for i in range(n):
        for j in range(m):
            print(i+(j+1), end=' ')
        print()
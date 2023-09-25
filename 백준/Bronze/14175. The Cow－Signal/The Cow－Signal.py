import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for _ in range(k):
        for j in range(m):
            for _ in range(k):
                print(arr[i][j], end='')
        
        print()
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    input()
    r, c = map(int, input().rstrip().split())
    maps = [list(input().rstrip()) for _ in range(r)]

    cnt = 0
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'o':
                # Sero
                if 0 <= i - 1 and maps[i-1][j] == 'v' and i + 1 < r and maps[i+1][j] == '^':
                    cnt += 1
                # Garo
                if 0 <= j - 1 and maps[i][j-1] == '>' and j + 1 < c and maps[i][j+1] == '<':
                    cnt += 1
    
    print(cnt)
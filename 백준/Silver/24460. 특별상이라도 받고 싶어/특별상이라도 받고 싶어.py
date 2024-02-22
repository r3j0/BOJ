import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

def func(now, u, l, d, r):
    if now == 1:
        return arr[u][l]
    else:
        go = [func(now//2, u, l, (d+u)//2, (r+l)//2), func(now//2, u, (r+l)//2+1, (d+u)//2, r), func(now//2, (d+u)//2+1, l, d, (r+l)//2), func(now//2, (d+u)//2+1, (r+l)//2+1, d,r)]
        go.sort()
        return go[1]

print(func(n, 0, 0, n-1, n-1))
import sys 
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = []
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    now_arr = []
    for i in range(m):
        now_arr.append([arr[i*3], arr[i*3+1], arr[i*3+2]])
    maps.append(now_arr)

def intensity(a):
    now = a[0]*2126 + a[1]*7152 + a[2]*722
    if now < 510000: return '#'
    elif now < 1020000: return 'o'
    elif now < 1530000: return '+'
    elif now < 2040000: return '-'
    else: return '.'

for i in range(n):
    for j in range(m):
        print(intensity(maps[i][j]), end='')
    print()
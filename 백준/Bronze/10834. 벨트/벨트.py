import sys
input = sys.stdin.readline

m = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]

now_dir = 0
now_loop = 1
for i in range(m):
    now_loop = now_loop * arr[i][1] // arr[i][0]

    if arr[i][2] == 1:
        now_dir = 1 if now_dir == 0 else 0

print(now_dir, now_loop)
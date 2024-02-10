import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

result = []
arr = [[0 for _ in range(n)] for _ in range(n)]

now = [n//2, n//2]

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
dir = 0
cnt = 0
num = 1
num_plus_cnt = 0

now_num = 1
while 0 <= now[0] < n and 0 <= now[1] < n:
    if now_num == k:
        result = [now[0], now[1]]
    
    arr[now[0]][now[1]] = now_num
    now_num += 1

    now[0] += row[dir]
    now[1] += col[dir]

    cnt += 1
    if num == cnt:
        cnt = 0
        dir = (dir + 1) % 4

        num_plus_cnt += 1
        if num_plus_cnt == 2: 
            num += 1
            num_plus_cnt = 0


for i in range(n): print(' '.join(map(str, arr[i])))
print(result[0]+1, result[1]+1)
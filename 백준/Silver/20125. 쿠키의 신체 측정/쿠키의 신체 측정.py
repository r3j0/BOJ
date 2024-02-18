import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(input().rstrip()) for _ in range(n)]
result1 = [0, 0]
result2 = [0, 0, 0, 0, 0]

for i in range(n):
    for j in range(n):
        if arr[i][j] == '*':
            result1 = [i+2, j+1]

            now = [i+1, j-1]
            cnt = 0
            while 0 <= now[0] < n and 0 <= now[1] < n and arr[now[0]][now[1]] == '*': 
                cnt += 1
                now[1] -= 1
            result2[0] = cnt

            now = [i+1, j+1]
            cnt = 0
            while 0 <= now[0] < n and 0 <= now[1] < n and arr[now[0]][now[1]] == '*': 
                cnt += 1
                now[1] += 1
            result2[1] = cnt

            now = [i+2, j]
            cnt = 0
            while 0 <= now[0] < n and 0 <= now[1] < n and arr[now[0]][now[1]] == '*': 
                cnt += 1
                now[0] += 1
            result2[2] = cnt

            now_l = [now[0], now[1]-1]
            cnt = 0
            while 0 <= now_l[0] < n and 0 <= now_l[1] < n and arr[now_l[0]][now_l[1]] == '*': 
                cnt += 1
                now_l[0] += 1
            result2[3] = cnt

            now_r = [now[0], now[1]+1]
            cnt = 0
            while 0 <= now_r[0] < n and 0 <= now_r[1] < n and arr[now_r[0]][now_r[1]] == '*': 
                cnt += 1
                now_r[0] += 1
            result2[4] = cnt
            
            break
    if result1[0] != 0: break

print(' '.join(map(str, result1)))
print(' '.join(map(str, result2)))
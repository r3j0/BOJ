import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) + [0, 0] for _ in range(n)]
arr.sort(key=lambda x:x[0])

t = 0
now_pos = 0
now_color = 0
while now_pos < l:
    for i in range(n):
        arr[i][4] += 1
        if arr[i][3] == 0 and arr[i][1] == arr[i][4]:
            arr[i][3] = 1
            arr[i][4] = 0
        elif arr[i][3] == 1 and arr[i][2] == arr[i][4]:
            arr[i][3] = 0
            arr[i][4] = 0

    if now_color < n and arr[now_color][0] == now_pos:
        if arr[now_color][3] == 1:
            now_pos += 1
            now_color += 1
    else:
        now_pos += 1
        
    t += 1

print(t+1)
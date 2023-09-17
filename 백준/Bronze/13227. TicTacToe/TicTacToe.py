import sys
input = sys.stdin.readline

arr = [list(input().rstrip()) for _ in range(3)]
res = 0

# Garo
for i in range(3):
    if arr[i][0] != '.' and arr[i].count(arr[i][0]) == 3:
        res = 1
# Sero
for j in range(3):
    cnt = 0
    for i in range(3):
        if arr[i][j] == 'O': cnt += 1
        elif arr[i][j] == 'X': cnt -= 1
    
    if cnt == 3 or cnt == -3: res = 1
# Daegak
cnt = 0
for i in range(3):
    if arr[i][i] == 'O': cnt += 1
    elif arr[i][i] == 'X': cnt -= 1

if cnt == 3 or cnt == -3: res = 1

cnt = 0
for i in range(3):
    if arr[i][2-i] == 'O': cnt += 1
    elif arr[i][2-i] == 'X': cnt -= 1

if cnt == 3 or cnt == -3: res = 1

print('YES' if res == 1 else 'NO')
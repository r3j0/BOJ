import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(r)]
arr = []
for i in range(r):
    for k in range(1, 10):
        if maps[i].count(str(k)) > 0:
            cnt = 0
            for j in range(c-1, -1, -1):
                if maps[i][j] == str(k):
                    break
                cnt += 1
            arr.append([cnt, k, 0])

arr.sort(key=lambda x:x[0])
arr[0][2] = 1
now = 1
for i in range(1, len(arr)):
    if arr[i][0] != arr[i-1][0]:
        now += 1
    arr[i][2] = now
arr.sort(key=lambda x:x[1])
for i in range(len(arr)):
    print(arr[i][2])
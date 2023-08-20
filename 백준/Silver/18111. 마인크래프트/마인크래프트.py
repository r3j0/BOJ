import sys
input = sys.stdin.readline

n, m, b = map(int, input().rstrip().split())
maps = []
max_h = 0
min_h = 256
for _ in range(n):
    tmp = list(map(int, input().rstrip().split()))
    max_h = max(max_h, max(tmp))
    min_h = min(min_h, min(tmp))
    maps.append(tmp)
time = 128000001
res_height = 0
for h in range(min_h, max_h + 1):
    cnt = 0
    now_b = b
    for i in maps:
        for j in i:
            if j > h:
                cnt += (j - h) * 2
                now_b += j - h
            elif j < h:
                cnt += (h - j)
                now_b -= h - j
            
    if (time >= cnt and now_b >= 0):
        time = cnt
        res_height = h

print(time, res_height)
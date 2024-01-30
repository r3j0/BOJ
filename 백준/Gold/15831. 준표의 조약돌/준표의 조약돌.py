# B가 Z개 이하이고 W가 Y개 이상인 가장 긴 구간의 길이
import sys
input = sys.stdin.readline

n, z, y = map(int, input().rstrip().split())
arr = list(input().rstrip())

start = 0 # 첫번째만
end = 1 

now_b = 0
now_w = 0

result = 0
if arr[0] == 'W': now_w += 1
else: now_b += 1
while start < n or end < n:
    if now_b <= z and now_w >= y: 
        result = max(result, end - start)
    if now_b <= z and end < n:
        if arr[end] == 'W': now_w += 1
        else: now_b += 1
        end += 1
    else:
        if arr[start] == 'W': now_w -= 1
        else: now_b -= 1
        start += 1

        if start == end and end < n:
            if arr[end] == 'W': now_w += 1
            else: now_b += 1
            end += 1

print(result)
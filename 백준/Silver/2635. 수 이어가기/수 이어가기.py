import sys
input = sys.stdin.readline

n = int(input().rstrip())
max_arr = []
for i in range(1, n+1):
    now_arr = [n, i]
    while True:
        if now_arr[-2] - now_arr[-1] < 0: break
        now_arr.append(now_arr[-2] - now_arr[-1])
    
    if len(now_arr) > len(max_arr): max_arr = list(now_arr)

print(len(max_arr))
print(' '.join(map(str, max_arr)))
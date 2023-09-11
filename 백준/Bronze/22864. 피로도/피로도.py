import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().rstrip().split())

now_time = 0
now_piro = 0
now_work = 0
while now_time < 24:
    if now_piro + a > m:
        now_piro = max(0, now_piro - c)
    else:
        now_piro += a
        now_work += b
    
    now_time += 1

print(now_work)
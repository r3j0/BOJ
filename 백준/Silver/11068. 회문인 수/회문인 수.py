import sys
input = sys.stdin.readline

def jinsu(num, p):
    string = []
    now = num
    while num >= 1:
        now = num % p
        string.append(now)
        num //= p
    
    if num != 0: string.append(now)
    return string

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    done = 0
    for i in range(2, 65):
        now_arr = jinsu(n, i)
        if now_arr == now_arr[::-1]:
            done = 1
            break
    print(done)
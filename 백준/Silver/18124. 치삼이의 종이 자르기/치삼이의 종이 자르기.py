import sys
input = sys.stdin.readline

n = int(input())

if n == 1: print(0)
else:
    if n % 2 == 1: n += 1

    now_bit = 0
    cnt_bit = 0
    up_bit = 1
    while 1 << now_bit <= n:
        if (n & (1 << now_bit)) >> now_bit: 
            cnt_bit += 1
            up_bit = now_bit
        now_bit += 1
    if cnt_bit > 1: now_n = 2 ** (up_bit + 1)
    elif cnt_bit == 0: now_n = 2 ** now_bit
    else: now_n = 2 ** up_bit

    print(now_n - 1 - ((now_n - n) // 2))
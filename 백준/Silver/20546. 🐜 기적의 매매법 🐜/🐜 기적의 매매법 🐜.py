import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

# BNF
bnf_money = n
bnf_cnt = 0
for a in arr:
    bnf_cnt += (bnf_money // a)
    bnf_money %= a

bnf_money += arr[-1] * bnf_cnt

# TIMING
timing_money = n
timing_cnt = 0

timing_updown = 0
for i in range(1, 14):
    if arr[i] - arr[i-1] > 0: # 상승
        if timing_updown >= 0: timing_updown += 1
        else: timing_updown = 1
    elif arr[i] - arr[i-1] < 0: # 하락
        if timing_updown <= 0: timing_updown -= 1
        else: timing_updown = -1
    else: # 동등
        timing_updown = 0

    if timing_updown <= -3:
        timing_cnt += (timing_money // arr[i])
        timing_money %= arr[i]

    elif timing_updown >= 3:
        timing_money += (timing_cnt * arr[i])
        timing_cnt = 0

timing_money += (timing_cnt * arr[-1])

print('SAMESAME' if bnf_money == timing_money else ('BNP' if bnf_money > timing_money else 'TIMING'))

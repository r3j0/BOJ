import sys
input = sys.stdin.readline

order = []

an = int(input())
for _ in range(an): order.append([int(input()), 1])

bn = int(input())
for _ in range(bn): order.append([int(input()), 2])

order.sort(key=lambda x:x[0])

ascore = 0
bscore = 0
before_cnt = 0
cnt = 0
now = 0
for o in order:
    if ascore != 0 or bscore != 0:
        if ascore > bscore: now = -1
        elif ascore < bscore: now = 1
    else:
        now = 0

    if o[1] == 1: ascore += 1
    else: bscore += 1

    if o[0] <= 1440: before_cnt += 1

    if now != 0:
        if now == -1 and ascore < bscore: cnt += 1
        elif now == 1 and ascore > bscore: cnt += 1

print(before_cnt)
print(cnt)
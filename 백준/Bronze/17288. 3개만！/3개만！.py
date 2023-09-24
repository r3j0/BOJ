import sys
input = sys.stdin.readline

s = list(input().rstrip())
no_cnt = 0
cnt = 0
counting = 0
for i in range(len(s) - 1):
    if int(s[i]) + 1 == int(s[i + 1]):
        counting += 1
    else:
        if counting == 2:
            cnt += 1
        counting = 0
if counting == 2:
    cnt += 1
print(cnt)
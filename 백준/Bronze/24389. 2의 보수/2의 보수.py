import sys
input = sys.stdin.readline

n = int(input().rstrip())
bin_n = bin(n)[2:]
now = ('0'*(32-len(bin_n))) + bin_n
now_reverse = ""
for i in now:
    if i == '0': now_reverse += '1'
    else: now_reverse += '0'

now_reverse = bin(int(now_reverse, 2) + 1)[2:]
if len(now_reverse) < 32:
    now_reverse = ('0'*(32-len(now_reverse))) + now_reverse
elif len(now_reverse) > 32:
    now_reverse = now_reverse[len(now_reverse)-32:]

cnt = 0
for i in range(32):
    if now[i] != now_reverse[i]:
        cnt += 1

print(cnt)
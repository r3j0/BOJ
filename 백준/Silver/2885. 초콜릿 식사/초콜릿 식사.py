import sys
input = sys.stdin.readline

k = int(input().rstrip())

# 1. 2의 거듭제곱인지 확인
nk = k
while nk >= 2:
    if nk % 2 == 0:
        nk //= 2
    else:
        break

if nk == 1: print(2**(len(bin(k)[2:])-1), 0)
else: 
    result = -1
    now = bin(k)[2:]
    for i in range(len(now)):
        if now[i] == '1':
            result = i + 1
    print(2**(len(now)), result)

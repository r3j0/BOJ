import sys
input = sys.stdin.readline

n, macMin, macMax, macUp, macDown = map(int, input().rstrip().split())
cnt = 0
time = 0
notundong = 0
nowmac = macMin
while True:
    if nowmac + macUp <= macMax:
        nowmac += macUp
        cnt += 1
        notundong = 0
    else:
        if notundong == macUp + 1: break
        nowmac = max(macMin, nowmac - macDown)
        notundong += 1
    time += 1
    if cnt == n: break

print(time if notundong != macUp + 1 else -1)
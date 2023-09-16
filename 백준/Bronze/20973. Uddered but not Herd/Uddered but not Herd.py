import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

aidx = 0
idx = 0
cnt = 1
while True:
    if a[aidx] == b[idx]:
        idx += 1
        if idx == len(b):
            break
    aidx += 1
    if aidx == len(a):
        aidx = 0
        cnt += 1

print(cnt)
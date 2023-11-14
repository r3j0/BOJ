import sys
input = sys.stdin.readline

x = int(input())

now = 64 #1000000
idx = 6

store = 0 #0000000

while x != 0:
    if now <= x:
        x -= now

        store |= (1 << idx)
        if x == 1: 
            store |= 1
            break

    now //= 2
    idx -= 1

cnt = 0
for i in range(7):
    if (store & (1 << i)) >> i == 1: cnt += 1

print(cnt)
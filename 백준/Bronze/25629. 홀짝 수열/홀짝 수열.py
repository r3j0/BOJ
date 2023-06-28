import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

odd = 0
even = 0
for a in arr:
    if a % 2 == 0: even += 1
    else: odd += 1

if n % 2 == 1:
    if odd - 1 == even: print(1)
    else: print(0)
else:
    if odd == even: print(1)
    else: print(0)
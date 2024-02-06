import sys
input = sys.stdin.readline

sums = 0
xors = 0

m = int(input().rstrip())
for _ in range(m):
    order = list(map(int, input().rstrip().split()))
    if order[0] == 1:
        sums += order[1]
        xors ^= order[1]
    elif order[0] == 2:
        sums -= order[1]
        xors ^= order[1]
    elif order[0] == 3:
        print(sums)
    else:
        print(xors)
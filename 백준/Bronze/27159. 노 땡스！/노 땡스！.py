import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

now = []
order = []
for a in arr:
    if len(now) == 0:
        now.append(a)
    else:
        if now[-1] + 1 == a:
            now.append(a)
        else:
            order.append(now[0])
            now = [a]
if len(now) > 0: order.append(now[0])
print(sum(order))
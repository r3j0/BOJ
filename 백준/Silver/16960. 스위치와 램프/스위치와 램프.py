import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = []
lamp = [0 for _ in range(m+1)]
for _ in range(n):
    order = list(map(int, input().rstrip().split()))[1:]
    arr.append(order)
    for o in order:
        lamp[o] += 1
del lamp[0]
done = True
if min(lamp) == 0: done = False
cnt = 0
for i in range(n):
    ccnt = 0
    for j in arr[i]:
        if lamp[j-1] == 1:
            ccnt = 1
    cnt += ccnt
if cnt == n: done = False
print(1 if done else 0)
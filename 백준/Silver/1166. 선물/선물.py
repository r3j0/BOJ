import sys
import math
input = sys.stdin.readline

n, l, w, h = map(int, input().rstrip().split())
start = 0
end = min([l, w, h])
done = 0
res = start
for _ in range(100000):
    mid = (start + end) / 2
    if math.floor(l/mid) * math.floor(w/mid) * math.floor(h/mid) >= n:
        start = mid
        res = max(res, start)
    else:
        end = mid
print(res)
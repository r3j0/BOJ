import sys
input = sys.stdin.readline

n, k, i = map(int, input().rstrip().split())

k -= 1
i -= 1

for c in range(20):
    if (k == i):
        print(c)
        break
    k //= 2
    i //= 2
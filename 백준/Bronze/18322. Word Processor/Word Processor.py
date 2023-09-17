import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(input().rstrip().split())

lens = 0
now = ""
for a in arr:
    if lens + len(a) <= k:
        lens += len(a)
        if now != "":
            now += " "
        now += a
    else:
        print(now)
        lens = len(a)
        now = a
print(now)
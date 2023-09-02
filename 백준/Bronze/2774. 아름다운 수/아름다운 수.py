import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    x = input().rstrip()
    arr = [x.count(str(i)) for i in range(10)]

    cnt = 0
    for a in arr:
        if a > 0:
            cnt += 1

    print(cnt)
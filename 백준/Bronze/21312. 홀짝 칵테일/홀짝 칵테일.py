arr = list(map(int, input().rstrip().split()))
cntodd = 0
for a in arr:
    if a % 2 == 1: cntodd += 1

if cntodd > 0:
    res = 1
    for a in arr:
        if a % 2 == 1: res *= a
    print(res)
else:
    res = 1
    for a in arr:
        res *= a
    print(res)
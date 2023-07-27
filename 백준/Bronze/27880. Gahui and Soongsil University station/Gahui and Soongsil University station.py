now = 0
for i in range(4):
    e, n = input().split()
    if e == "Es": now += (int(n) * 21)
    else: now += (int(n) * 17)

print(now)
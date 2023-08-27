import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().rstrip().split())
p, m, n = map(int, input().rstrip().split())

def dogfight(end, atkTime, noTime):
    mode = 0
    # 0 : 공격 중
    # 1 : 쉬는 중
    time = 1
    while True:
        if mode == 0:
            time += atkTime
        else:
            time += noTime

        if time > end: break
        mode = 0 if mode == 1 else 1

    if mode == 0: return 1
    else: return 0

# 우체부
print(dogfight(p, a, b) + dogfight(p, c, d))

# 신문배달원
print(dogfight(m, a, b) + dogfight(m, c, d))

# 우유배달원
print(dogfight(n, a, b) + dogfight(n, c, d))
import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
def func(now):
    global cnt
    if now <= 1: return

    cnt += (now // 2) * (now - (now // 2))
    func((now // 2))
    func((now - (now // 2)))

func(n)
print(cnt)
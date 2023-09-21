import sys
input = sys.stdin.readline

n = input().rstrip()
now = "1"
num = 2
lencnt = 0
while True:
    while len(n)*2 > len(now):
        now += str(num)
        num += 1
    
    if now.find(n) == -1:
        now = now[len(n):]
        lencnt += len(n)
    else:
        lencnt += now.index(n)
        break

print(lencnt + 1)
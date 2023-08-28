import sys
input = sys.stdin.readline

now = int(input().rstrip())
cnt = 0
while len(str(now)) != 1:
    new_now = 1
    for s in list(str(now)):
        new_now *= int(s)
    now = new_now
    
    cnt += 1
print(cnt)
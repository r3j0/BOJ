import sys
input = sys.stdin.readline

n = int(input().rstrip())

now = 1
su = 1
last_check = 1

while now <= 32:
    if ((su << (now - 1)) & n) >> (now - 1) == 1:
        last_check = now
    now += 1

print(last_check)
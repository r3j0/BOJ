import sys
input = sys.stdin.readline

n = int(input().rstrip())
now = n%10*10+(n//10+n%10)%10
cnt = 1

while now != n:
    now = now%10*10+(now//10+now%10)%10
    cnt += 1

print(cnt)
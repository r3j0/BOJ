import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d = map(int, input().rstrip().split())

now_value = -1
now_cnt = 5

for i in range(4):
    a, b, c, d = c, a, d, b
    if (now_value < (a//c + b//d)):
        now_value = a//c + b//d
        now_cnt = i + 1

print(now_cnt % 4)
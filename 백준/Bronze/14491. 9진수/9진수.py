import sys
input = sys.stdin.readline

t = int(input().rstrip())

def nine(num):
    now = num
    if num >= 9:
        now = num % 9
        nine(num // 9)
    print(now, end='')

nine(t)
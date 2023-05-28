import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break
    print((n+1)//2)
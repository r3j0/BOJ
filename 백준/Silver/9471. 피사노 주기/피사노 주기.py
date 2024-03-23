# 9471 : 피사노 주기
# 0 과 1이 나올때까지 주기 구하기

import sys
input = sys.stdin.readline

p = int(input().rstrip())
for _ in range(p):
    n, m = map(int, input().rstrip().split())
    first = 0
    second = 1
    cnt = 0
    while True:
        now = (first + second) % m
        first = second
        second = now
        cnt += 1

        if first == 0 and second == 1: break
    print(n, cnt)
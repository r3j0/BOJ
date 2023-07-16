import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b, c = map(int, input().rstrip().split())
    cnt = 0
    for a1 in range(1, a+1):
        for b1 in range(1, b+1):
            for c1 in range(1, c+1):
                if a1 % b1 == b1 % c1 == c1 % a1: cnt += 1
    print(cnt)
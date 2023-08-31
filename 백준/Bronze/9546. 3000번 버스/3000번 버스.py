import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    k = int(input().rstrip())
    now = 1
    for _ in range(k - 1):
        now = (now + 1) * 2 - 1
    print(now)
    

# n명
# n//2 + 0.5  -> 0 / 마지막 n 1
# n//2 + 0.5  -> 1 / 3
# 7
# 15
# 31
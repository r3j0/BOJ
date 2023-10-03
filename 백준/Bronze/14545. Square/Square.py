import sys
input = sys.stdin.readline

n = int(input().rstrip())
sums = 0
for _ in range(n):
    tmp = int(input().rstrip())
    print(tmp*(tmp+1)*(2*tmp+1)//6)
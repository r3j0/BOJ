import sys
input = sys.stdin.readline

n = int(input().rstrip())
mx, my = map(int, input().rstrip().split())
for _ in range(n-1):
    x, y = map(int, input().rstrip().split())
    if my > y: 
        mx = x
        my = y
print(mx, my)
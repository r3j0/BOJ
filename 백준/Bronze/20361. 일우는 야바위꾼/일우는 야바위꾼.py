import sys
input = sys.stdin.readline 

n, x, k = map(int, input().rstrip().split())

for _ in range(k):
    a, b = map(int, input().rstrip().split())
    if a == x:
        x = b
    elif b == x:
        x = a

print(x)
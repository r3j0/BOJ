import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())
mins = x*(1000/y)

n = int(input().rstrip())
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    mins = min(mins, a*(1000/b))

print('%.2f'%mins)
import sys
input = sys.stdin.readline 

a, b, c, x, y = map(int, input().rstrip().split())
result = x*a+y*b
banban = 2
while banban // 2 <= x or banban // 2 <= y:
    result = min(result, banban*c + (max(0, x - (banban//2)) * a) + (max(0, y - (banban//2)) * b))
    banban += 2

print(result)
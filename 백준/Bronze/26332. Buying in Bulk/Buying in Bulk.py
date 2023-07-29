n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a, b)
    print(a*b - (0 if a <= 1 else 2*(a-1)))
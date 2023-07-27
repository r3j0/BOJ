n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y):
        print('X' * x)
    print()
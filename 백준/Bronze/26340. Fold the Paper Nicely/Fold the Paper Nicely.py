n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    print('Data set:',a,b,c)
    for i in range(c):
        if a > b: a //= 2
        else: b //= 2
    print(max(a, b), min(a, b))
    print()
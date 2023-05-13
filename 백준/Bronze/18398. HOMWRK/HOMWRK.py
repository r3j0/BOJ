t = int(input())
for test in range(t):
    n = int(input())
    for num in range(n):
        a, b = map(int, input().split())
        print(a+b, a*b)
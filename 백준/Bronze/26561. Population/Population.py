t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a-(b//7)+(b//4))
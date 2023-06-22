t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    for i in range(n):
        a, b, c = input().split()
        sum += float(b) * float(c)
    print('$%.2f'%sum)
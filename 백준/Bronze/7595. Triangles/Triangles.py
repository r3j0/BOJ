def go(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()

while True:
    a = int(input())
    if a == 0: break
    go(a)
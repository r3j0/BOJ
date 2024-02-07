while True:
    n = int(input().rstrip())
    if n == 0: break
    arr = [int(input().rstrip()) for _ in range(n)]
    for a in arr[::-1]: print(a)
    print(0)
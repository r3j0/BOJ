n = int(input())
for _ in range(n):
    print('@@@@@'*n)
for _ in range(3):
    for _ in range(n):
        print(('@'*n) + ('   '*n) + ('@'*n))
for _ in range(n):
    print('@@@@@'*n)
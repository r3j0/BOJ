n, m, k = map(int, input().rstrip().split())
print(n // (k - m) + (1 if n % (k - m) != 0 else 0))
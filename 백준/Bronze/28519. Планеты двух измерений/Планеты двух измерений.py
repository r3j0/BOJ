a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
print(min(a+(a+1), a+b))
k = int(input().rstrip())
d1, d2 = map(int, input().rstrip().split())

print(((k**2)-((abs(d1-d2)/2)**2)))
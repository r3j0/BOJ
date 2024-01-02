t = int(input())
for _ in range(t):
    s = input().rstrip()
    if s[-1] == '.': print(s)
    else: print(s + '.')
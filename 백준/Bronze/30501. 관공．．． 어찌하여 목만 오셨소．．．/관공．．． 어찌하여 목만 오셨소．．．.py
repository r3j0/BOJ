n = int(input())
arr = [input().rstrip() for _ in range(n)]
for a in arr:
    if a.count('S') > 0: print(a)

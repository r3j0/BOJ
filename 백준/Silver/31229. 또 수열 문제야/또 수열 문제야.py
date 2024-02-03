n = int(input().rstrip())
arr = [(i*2 - 1) for i in range(1, n+1)]
print(' '.join(map(str, arr)))
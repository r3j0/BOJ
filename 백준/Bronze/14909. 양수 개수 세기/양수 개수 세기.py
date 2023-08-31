arr = list(map(int, input().rstrip().split()))
result = 0
for a in arr:
    if a > 0: result += 1
print(result)
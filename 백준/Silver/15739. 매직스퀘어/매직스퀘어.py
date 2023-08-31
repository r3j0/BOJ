import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

nums = {i:0 for i in range(1, n**2+1)}
result = 0
# Garo
for i in range(n):
    sums = 0
    for j in range(n):
        if nums[arr[i][j]] == 1:
            result = 1
        nums[arr[i][j]] = 1
        sums += arr[i][j]
    
    if sums != (n*(n**2+1)//2):
        result = 1

# Sero
if result == 0:
    for j in range(n):
        sums = 0
        for i in range(n):
            sums += arr[i][j]
        
        if sums != (n*(n**2+1)//2):
            result = 1

# Daegak
if result == 0:
    sums = 0
    for i in range(n):
        sums += arr[i][i]
    if sums != (n*(n**2+1)//2):
        result = 1

    sums = 0
    for i in range(n):
        sums += arr[n-1-i][i]
    if sums != (n*(n**2+1)//2):
        result = 1

print('TRUE' if result == 0 else 'FALSE')
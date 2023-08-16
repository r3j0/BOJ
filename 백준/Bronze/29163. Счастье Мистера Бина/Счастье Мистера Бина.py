n = int(input())
arr = list(map(int, input().split()))
odd = 0
even = 0
for a in arr:
    if a % 2 == 1: odd += 1
    else: even += 1
if odd < even: print('Happy')
else: print('Sad')
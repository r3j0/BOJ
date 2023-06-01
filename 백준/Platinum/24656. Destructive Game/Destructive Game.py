import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    if b % 2 == 0:
        if (a % (b + 1) == b): arr.append(3)
        elif (a % (b + 1) % 2 == 0): continue
        else: arr.append(1)
    else:
        if (a % 2 == 0): continue
        else: arr.append(1)
    
result = 0
for a in arr: result ^= a
print('Alice' if result != 0 else 'Bob')
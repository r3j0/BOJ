import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = input().rstrip().split()
    zerotoone = 0
    onetozero = 0
    for i in range(len(n)):
        if n[i] != m[i]: 
            if n[i] == '0': onetozero += 1
            else: zerotoone += 1
    
    print(min(onetozero, zerotoone) + abs(onetozero-zerotoone))
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    score = 0
    jum = 0
    for _ in range(n):
        a, b = map(float, input().rstrip().split())
        score += a
        jum += a*b
    
    print(int(score), '%.1f'%(jum / score))
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    result = 0
    for i in range(n, m+1):
        result += str(i).count('0')
    
    print(result)
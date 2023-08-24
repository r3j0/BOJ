import sys
input = sys.stdin.readline

n = int(input().rstrip())
name = [input().rstrip() for _ in range(n)]

k = int(input().rstrip())
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    for i in range(a, b+1):
        print(name[i-1])
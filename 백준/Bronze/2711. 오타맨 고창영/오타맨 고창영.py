import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, string = input().split()
    print(string[:int(n)-1] + string[int(n):])
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    input()
    n = int(input().rstrip())
    arr = [int(input().rstrip()) for _ in range(n)]

    print('YES' if sum(arr) % n == 0 else 'NO')
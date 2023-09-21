import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    arr = list(sorted(map(int, input().rstrip().split())))
    print(arr[m-1])
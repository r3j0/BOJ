import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
result = sum(arr) + ((n - 1) * 8)
print(result//24, result%24)
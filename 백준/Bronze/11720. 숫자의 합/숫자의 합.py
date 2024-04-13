import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, list(input().rstrip())))
print(sum(arr))
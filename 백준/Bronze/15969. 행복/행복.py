import sys
input = sys.stdin.readline

_ = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
print(max(arr) - min(arr))
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

v = int(input().rstrip())
print(arr.count(v))
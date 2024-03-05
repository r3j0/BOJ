import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(input().rstrip().split())
now = input().rstrip()
print(arr.count(now))
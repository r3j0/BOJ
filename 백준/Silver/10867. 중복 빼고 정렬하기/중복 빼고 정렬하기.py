import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(set(map(int, input().rstrip().split())))
print(' '.join(map(str, arr)))
import sys
input = sys.stdin.readline

n = int(input().rstrip())
res1 = [1] * 999
res2 = [1000] * 1000
print(len(res1) + len(res2))
print(' '.join(map(str, res1 + res2)))
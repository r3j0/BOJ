import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [float(input().rstrip()) for _ in range(n)]
arr.sort()
for i in range(7): print('%.3f'%arr[i])
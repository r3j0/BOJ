import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
res = 0
for i in range(n):
    res += int(math.sqrt((arr[i][0] - arr[(i+1)%n][0])**2 + (arr[i][1] - arr[(i+1)%n][1])**2))
print(res)
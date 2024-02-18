import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    result = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            result = max(result, math.gcd(arr[i], arr[j]))
    print(result)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0

arr = list(map(int, input().rstrip().split()))
for i in range(n):
    for j in range(i):
        result += abs(arr[i] - arr[j])
print(result * 2)
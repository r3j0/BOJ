import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort(reverse=True)

result = 0
for i in range(1, n): result += arr[0] + arr[i]
print(result)
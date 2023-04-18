import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
arrSum = []
arrSum.append(arr[0])
for a in range(1, n):
    arrSum.append(arrSum[-1] + arr[a])
result = 0
for i in range(n - 1):
    result += arr[i] * (arrSum[n - 1] - arrSum[i])

print(result)
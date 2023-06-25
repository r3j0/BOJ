import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = sorted(map(int, input().rstrip().split()))

sum = 0
for i in range(n-1):
    sum += abs(arr[i] - arr[i+1])
sum += abs(arr[n-1] - arr[0])

print(sum)
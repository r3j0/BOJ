import sys
input = sys.stdin.readline

n, q = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

prefixSum = [0]
prefixSqSum = [0]

for a in arr:
    prefixSum.append(a+prefixSum[-1])
    prefixSqSum.append(a**2+prefixSqSum[-1])

for _ in range(q):
    l, r = map(int, input().rstrip().split())
    print(((prefixSum[r] - prefixSum[l-1])**2 - (prefixSqSum[r] - prefixSqSum[l-1]))//2)
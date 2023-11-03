import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

max_value = 0
for c1 in range(n-2):
    for c2 in range(c1+1, n-1):
        for c3 in range(c2+1, n):
            if arr[c1] + arr[c2] + arr[c3] <= m and max_value < arr[c1] + arr[c2] + arr[c3]:
                max_value = arr[c1] + arr[c2] + arr[c3]
    
print(max_value)
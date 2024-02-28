import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr6 = []
arr1 = []
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    arr6.append(a)
    arr1.append(b)

arr6.sort()
arr1.sort()
print(min(arr6[0]*(n//6)+(arr6[0] if n%6 != 0 else 0), arr6[0]*(n//6)+arr1[0]*(n%6), arr1[0]*n))
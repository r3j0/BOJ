import sys
input = sys.stdin.readline
s, k = map(int, input().rstrip().split())

arr = [(s//k) for _ in range(k)]
for i in range(s%k):
    arr[i] += 1
print(eval('*'.join(map(str, arr))))
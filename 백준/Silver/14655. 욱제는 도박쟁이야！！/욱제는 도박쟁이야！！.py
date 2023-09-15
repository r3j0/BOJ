import sys
input = sys.stdin.readline 

n = int(input().rstrip())
aArr = list(map(int, input().rstrip().split()))
bArr = list(map(int, input().rstrip().split()))

res = 0
for i in range(n):
    res += abs(aArr[i]) + abs(bArr[i])

print(res)
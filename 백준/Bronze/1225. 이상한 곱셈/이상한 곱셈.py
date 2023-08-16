import sys
input = sys.stdin.readline

aArr, bArr = input().rstrip().split()
result = 0
for a in aArr:
    for b in bArr:
        result += (int(a) * int(b))
print(result)
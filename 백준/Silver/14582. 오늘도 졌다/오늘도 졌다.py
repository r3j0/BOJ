import sys
input = sys.stdin.readline

aArr = list(map(int, input().rstrip().split()))
bArr = list(map(int, input().rstrip().split()))

a = 0
b = 0
done = False
for i in range(9):
    a += aArr[i]
    if a > b: done = True
    b += bArr[i]

print('Yes' if done else 'No')
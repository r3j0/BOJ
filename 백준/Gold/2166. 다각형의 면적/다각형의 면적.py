import sys
input = sys.stdin.readline
n = int(input().rstrip())
arrX = []
arrY = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    arrX.append(a)
    arrY.append(b)

result1 = 0
result2 = 0
for i in range(n-1):
    result1 += arrX[i]*arrY[i+1]
    result2 += arrY[i]*arrX[i+1]
result1 += arrX[n-1]*arrY[0]
result2 += arrY[n-1]*arrX[0]

print('%.1f'%(abs(result1-result2)/2))
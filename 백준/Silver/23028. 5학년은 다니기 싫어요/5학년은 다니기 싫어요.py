n, a, b = map(int, input().rstrip().split())
arr = []
for _ in range(10):
    i, j = map(int, input().rstrip().split())
    arr.append([i, j])

for i in range(8-n):
    b += (min(6, arr[i][0]+arr[i][1])) * 3
    a += (min(6, arr[i][0])) * 3

if a >= 66 and b >= 130: print('Nice')
else: print('Nae ga wae')
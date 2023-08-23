import sys
input = sys.stdin.readline

arr = []
while True:
    now = float(input().rstrip())
    if now == 999: break
    arr.append(now)

for i in range(len(arr) - 1):
    print('%.2f'%(arr[i+1] - arr[i]))
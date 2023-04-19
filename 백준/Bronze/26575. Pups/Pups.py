test = int(input())
for t in range(test):
    arr = list(map(float, input().split()))
    print('$%.2f'%(arr[0]*arr[1]*arr[2]))

import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n != 0:
    arr = list(map(int, input().rstrip().split()))
    avgValue = sum(arr) / n
    expValue = 0
    for a in arr: expValue += a * (1/n)

    if expValue == 0: 
        print('divide by zero')
    else:
        print('%.2f'%(avgValue/expValue))
else:
    print('divide by zero')
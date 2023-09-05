import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    arr = list(sorted(map(int, input().rstrip().split())))
    if arr[0] + arr[1] > arr[2]:
        if arr[0] == arr[1] == arr[2]: print('Case #%d: equilateral'%i)
        elif arr[0] == arr[1] or arr[1] == arr[2]: print('Case #%d: isosceles'%i)
        else: print('Case #%d: scalene'%i)
    else: print('Case #%d: invalid!'%i)
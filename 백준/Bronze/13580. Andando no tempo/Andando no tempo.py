arr = list(map(int, input().rstrip().split()))
arr.sort()
if arr[0] == arr[1] or arr[1] == arr[2]:
    print('S')
elif arr[0] + arr[1] == arr[2]:
    print('S')
else:
    print('N')
import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 0: break
    dic = {}
    for a in range(1, arr[0]+1):
        if a == 1:
            print(arr[a], end=' ')
        else:
            if arr[a-1] != arr[a]:
                print(arr[a], end=' ')
    print('$')
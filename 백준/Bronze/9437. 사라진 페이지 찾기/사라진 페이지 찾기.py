import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 0: break

    if arr[1] <= arr[0] // 2:
        if arr[1] % 2 == 0:
            print(arr[1] - 1, arr[0] - (arr[1] - 1), arr[0] - (arr[1] - 1) + 1)
        else:
            print(arr[1] + 1, arr[0] - arr[1], arr[0] - arr[1] + 1)
    else:
        if arr[1] % 2 == 0:
            print(arr[0] - (arr[1] - 1), arr[0] - (arr[1] - 1) + 1, arr[1] - 1)
        else:
            print(arr[0] - arr[1], arr[0] - arr[1] + 1, arr[1] + 1)
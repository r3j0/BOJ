import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))

def bubblesort():
    global arr
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(' '.join(map(str, arr)))

while True:
    bubblesort()
    if arr == [1, 2, 3, 4, 5]: break
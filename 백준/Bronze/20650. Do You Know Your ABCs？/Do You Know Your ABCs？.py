import sys
input = sys.stdin.readline

arr = list(sorted(map(int, input().rstrip().split())))
done = 0
for i in range(4):
    for j in range(5):
        for k in range(6):
            if arr[i] + arr[j] + arr[k] == arr[-1]:
                print(arr[i], arr[j], arr[k])
                done = 1
                break
        if done == 1: break
    if done == 1: break
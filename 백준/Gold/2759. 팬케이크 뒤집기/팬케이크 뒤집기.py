import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, *arr = list(map(int, input().rstrip().split()))
    now = n
    result = []
    while now != 1 and arr != sorted(arr):
        if arr[0] != now:
            result.append(arr.index(now) + 1)
            arr = arr[:arr.index(now)+1][::-1] + arr[arr.index(now)+1:now] + arr[now:]
            result.append(now)
            arr = arr[:now][::-1] + arr[now:]
        else:
            result.append(now)
            arr = arr[:now][::-1] + arr[now:]
        now -= 1
    print(len(result), ' '.join(map(str, result)))
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()

result = 0
for i in range(n):
    start = 0
    end = n - 1

    if start == i: start += 1
    if end == i: end -= 1

    while start < end:
        if arr[start] + arr[end] == arr[i]:
            result += 1
            break

        if arr[start] + arr[end] >= arr[i]:
            end -= 1
        else:
            start += 1

        if start == i: start += 1
        if end == i: end -= 1

print(result)
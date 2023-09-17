import sys
input = sys.stdin.readline

t = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
for i in range(5-t):
    arr.append(0)

now = 0
if arr[0] > arr[2]: now += (abs(arr[0] - arr[2]) * 508)
else: now += (abs(arr[0] - arr[2]) * 108)
if arr[1] > arr[3]: now += (abs(arr[1] - arr[3]) * 212)
else: now += (abs(arr[1] - arr[3]) * 305)
if arr[4] > 0: now += arr[4] * 707

print(now * 4763)
import sys
import decimal
input = sys.stdin.readline

def roundUp(go):
    if (go - int(go)) >= 0.5:
        return int(go) + 1
    else:
        return int(go)

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

now = roundUp(n * 0.15)

if now * 2 >= n: print(0)
else:
    arr.sort()
    if now != 0: arr = arr[now:n-now]
    print(roundUp(sum(arr)/len(arr)))
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [input().rstrip() for _ in range(n)]

now = 0
result = ""

# First Find KBS
while arr[now] != "KBS1" and arr[now] != "KBS2":
    result += "1"
    now += 1

# Go First
while now != 0:
    arr[now - 1], arr[now] = arr[now], arr[now - 1]
    result += "4"
    now -= 1

now += 1
result += "1"
# Second Find KBS
while arr[now] != "KBS1" and arr[now] != "KBS2":
    result += "1"
    now += 1

if arr[now] == "KBS1":
    while now != 0:
        arr[now - 1], arr[now] = arr[now], arr[now - 1]
        result += "4"
        now -= 1
else:
    while now != 1:
        arr[now - 1], arr[now] = arr[now], arr[now - 1]
        result += "4"
        now -= 1

print(result)
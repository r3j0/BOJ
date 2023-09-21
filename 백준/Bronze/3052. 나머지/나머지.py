import sys
input = sys.stdin.readline

arr = [0 for _ in range(42)]
for _ in range(10):
    tmp = int(input().rstrip())
    arr[tmp % 42] = 1

print(sum(arr))
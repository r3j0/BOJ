import sys
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    input()
    arr = list(input().rstrip())
    arr.sort(reverse = True)
    print(int(''.join(arr[:-1])) + int(arr[-1]))
import sys
input = sys.stdin.readline

arr = [0 for _ in range(80001)]
for i in range(3, 80001):
    arr[i] = arr[i-1] + (i if i % 3 == 0 or i % 7 == 0 else 0)

t = int(input().rstrip())
order = list(map(int, input().rstrip().split()))
for o in order:
    print(arr[o])
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    arr = list(input().rstrip().split())

    arr[0] = 'god'
    print(''.join(arr))
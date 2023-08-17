t = int(input())
print(t)
for _ in range(t):
    input()
    n = int(input())
    arr = list(sorted(map(int, input().rstrip().split())))
    arr = arr[-1:] + arr[:-1]
    print()
    print(n)
    print(' '.join(map(str,arr)))
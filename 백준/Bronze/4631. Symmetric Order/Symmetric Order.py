import sys
input = sys.stdin.readline
t = 1
while True:
    n = int(input().rstrip())
    if n == 0: break

    arr = [input().rstrip() for _ in range(n)]
    keep = []
    print('SET', t)
    for i in range(n):
        if i % 2 == 1: keep.append(arr[i])
        else: print(arr[i])

    for k in keep[::-1]: print(k)
    t += 1
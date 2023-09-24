import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == -1: break

    arr = []
    pre = 0
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        arr.append([a, b-pre])
        pre = b
    
    sums = 0
    for a, b in arr: sums += a * b

    print('%d miles'%sums)
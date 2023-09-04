import sys
input = sys.stdin.readline

while True:
    try:
        n, k = map(int, input().rstrip().split())
    except:
        break

    result = n
    last = n
    while last >= k:
        result += last // k
        go = last // k
        last %= k
        last += go
    print(result)
        
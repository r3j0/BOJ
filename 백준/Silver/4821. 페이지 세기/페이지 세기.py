import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break

    available = [0 for _ in range(n+1)]

    arr = list(input().rstrip().split(','))

    for a in arr:
        if '-' in a:
            first, second = map(int, a.split('-'))
            if first > second: continue

            for i in range(first, min(n, second)+1): available[i] = 1
        else:
            if int(a) < n+1:
                available[int(a)] = 1
    
    print(sum(available))

               
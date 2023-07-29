import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    n, s, d = map(int, input().rstrip().split())
    darr = []
    varr = []
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        darr.append(a)
        varr.append(b)
    
    result = 0
    for k in range(n):
        if darr[k] // s + (0 if darr[k] % s == 0 else 1) <= d: 
            result += varr[k]
    
    print('Data Set %d:'%(i+1))
    print(result)

    print()
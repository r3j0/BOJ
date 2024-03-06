import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    arrA = list(map(int, input().rstrip().split()))
    arrB = list(map(int, input().rstrip().split()))

    dicA = {}
    for a in arrA: 
        if dicA.get(a): dicA[a] += 1
        else: dicA[a] = 1
    
    dicB = {}
    for b in arrB: 
        if dicB.get(b): dicB[b] += 1
        else: dicB[b] = 1
    
    res = 0
    lisA = list(dicA.items())
    lisA.sort(key=lambda x:x[0])
    lisB = list(dicB.items())
    lisB.sort(key=lambda x:x[0])

    for ak, av in lisA:
        for bk, bv in lisB:
            if ak > bk:
                res += av * bv
            else:
                break

    print(res)

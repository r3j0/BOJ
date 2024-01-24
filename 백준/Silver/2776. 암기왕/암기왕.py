import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr1 = list(map(int, input().rstrip().split()))

    dic = {}
    for a in arr1: dic[a] = 1

    m = int(input().rstrip())
    arr2 = list(map(int, input().rstrip().split()))

    for a in arr2: 
        if dic.get(a, -1) != -1: print(1)
        else: print(0)

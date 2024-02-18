import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr1 = list(input().rstrip().split())
    arr2 = list(input().rstrip().split())
    arr3 = list(input().rstrip().split())
    ind = [[i, 0] for i in range(n)]
    for i in range(n):
        ind[i][1] = arr2.index(arr1[i])
    
    for i in range(n):
        print(arr3[ind[i][1]], end=' ')
    print()
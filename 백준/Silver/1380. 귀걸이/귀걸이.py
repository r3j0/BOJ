import sys
input = sys.stdin.readline
t = 1
while True:
    n = int(input().rstrip())
    if n == 0: break

    names = [input().rstrip() for _ in range(n)]
    arr = [0 for _ in range(n)]
    for _ in range(2*n-1):
        a, b = input().rstrip().split()
        arr[int(a)-1] += 1
    
    print(t, names[arr.index(1)])
    t+= 1
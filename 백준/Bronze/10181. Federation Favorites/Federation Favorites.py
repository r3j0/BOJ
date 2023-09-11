import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == -1: break

    arr = []
    for i in range(1, n):
        if n % i == 0: arr.append(i)
    
    if sum(arr) == n:
        print('%d = '%(n) + ' + '.join(map(str, arr)))
    else:
        print('%d is NOT perfect.'%n)
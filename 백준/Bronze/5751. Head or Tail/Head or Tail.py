import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break

    arr = list(map(int, input().rstrip().split()))
    print('Mary won %d times and John won %d times'%(arr.count(0), arr.count(1)))
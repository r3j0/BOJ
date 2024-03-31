import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n == 1:
    print(0)
else:
    done = 0
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            print(n - (n // i))
            done = 1
            break
    if done == 0: print(n - 1)
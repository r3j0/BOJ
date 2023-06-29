import math
import sys
input = sys.stdin.readline

test = int(input().rstrip())
for _ in range(test):
    n = int(input().rstrip())

    done = 0
    while True:
        if n >= 9:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    done = 1
                    break
        else:
            if n >= 4:
                for i in range(2, n):
                    if n % i == 0:
                        done = 1
                        break
            else:
                if n <= 1:
                    n += 1
                    continue
                else:
                    done = 0
        
        if done == 0: break
        done = 0
        n += 1
    
    print(n)
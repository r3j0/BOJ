samgak = [(i*(i+1))//2 for i in range(1001)]

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    done = 0
    for i in range(1, 999):
        if n < samgak[i]:
                break
        for j in range(i, 1000):
            if n < samgak[i] + samgak[j]:
                    break
            for k in range(j, 1001):
                if n < samgak[i] + samgak[j] + samgak[k]:
                    break
                elif n == samgak[i] + samgak[j] + samgak[k]:
                    done = 1
                    break
            if done == 1: break
        if done == 1: break
    
    print(done)
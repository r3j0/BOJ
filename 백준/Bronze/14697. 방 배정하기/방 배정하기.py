import sys
input = sys.stdin.readline

a, b, c, n = map(int, input().rstrip().split())

done = 0
for i in range(0, n//a+1):
    for j in range(0, n//b+1):
        for k in range(0, n//c+1):
            if a*i+b*j+c*k==n: 
                done = 1
                break
        if done: break
    if done: break

print(done)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
k = 1
while True:
    done = True
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] % (10**k) == arr[j] % (10**k):
                done = False
                break
        if done == False: break 
    
    if done: break
    k += 1

print(k)
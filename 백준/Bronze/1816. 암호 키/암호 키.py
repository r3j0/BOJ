import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    num = int(input().rstrip())
    done = 0
    for i in range(2, 1000000):
        if num % i == 0: 
            done = 1
            break
    print('YES' if done == 0 else 'NO')
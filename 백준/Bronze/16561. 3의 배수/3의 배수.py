import sys
input = sys.stdin.readline

n = int(input().rstrip())
n //= 3

cnt = 0
for i in range(1, n):
    for j in range(i, n):
        if n < i+j: break
        for k in range(j, n):
            if n < i+j+k: break
            if n == i+j+k:
                if i == j == k: cnt += 1
                elif i == j or j == k or i == k: cnt += 3
                else: cnt += 6

print(cnt)
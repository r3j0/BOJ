import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(4):
    for _ in range(n):
        print('@'*n)

for _ in range(n):
    print('@@@@@'*n)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n): print(('@@@'*n)+(' '*n)+('@'*n))
for _ in range(n*3): print(('@'*n)+(' '*n)+('@'*n)+(' '*n)+('@'*n))
for _ in range(n): print(('@'*n)+(' '*n)+('@@@'*n))
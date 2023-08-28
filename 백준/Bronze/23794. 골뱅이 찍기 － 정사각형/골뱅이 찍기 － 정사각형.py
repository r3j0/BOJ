import sys
input = sys.stdin.readline

n = int(input().rstrip())

print('@'*(n+2))
for _ in range(n): print('@'+(' '*n)+'@')
print('@'*(n+2))
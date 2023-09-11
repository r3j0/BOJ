import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
digits = [0 for _ in range(10)]
for i in range(a, b+1):
    for j in range(10):
        digits[j] += (str(i)).count(str(j))

print(' '.join(map(str, digits)))

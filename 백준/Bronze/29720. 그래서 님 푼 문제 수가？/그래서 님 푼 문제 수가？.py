import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
print(n - (m * k) if n - (m * k) >= 0 else 0, (n - (m * k)) + (m - 1) if (n - (m * k)) + (m - 1) >= 0 else 0)
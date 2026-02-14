import sys
input = sys.stdin.readline

print('Yes' if sum([int(input().rstrip()) for _ in range(4)]) <= 1500 else 'No')
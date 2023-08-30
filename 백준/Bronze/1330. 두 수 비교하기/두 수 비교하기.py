import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
print('>' if a > b else ('<' if a < b else '=='))
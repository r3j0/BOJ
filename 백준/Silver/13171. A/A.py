import sys
input = sys.stdin.readline

def po(x, y):
    if y == 0: return 1
    if y == 1: return x % 1000000007
    if y % 2 == 0:
        return ((po(x, y//2) % 1000000007) ** 2) % 1000000007
    else:
        return ((po(x, y//2) % 1000000007) ** 2 * (x % 1000000007)) % 1000000007

a = int(input().rstrip())
x = int(input().rstrip())
print(po(a, x) % 1000000007)
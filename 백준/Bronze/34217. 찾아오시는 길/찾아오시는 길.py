import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d = map(int, input().rstrip().split())

print('Either' if a + c == b + d else ('Hanyang Univ.' if a + c < b + d else 'Yongdap'))
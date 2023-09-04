import sys
input = sys.stdin.readline

n = int(input().rstrip()) + 56
print(list('ABCDEFGHIJKL')[n % 12], end='')
print(list('0123456789')[n % 10])
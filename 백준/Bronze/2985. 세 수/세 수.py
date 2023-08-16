import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
if a + b == c: print('%d+%d=%d'%(a, b, c))
elif a - b == c: print('%d-%d=%d'%(a, b, c))
elif a * b == c: print('%d*%d=%d'%(a, b, c))
elif a // b == c: print('%d/%d=%d'%(a, b, c))
elif a == b + c: print('%d=%d+%d'%(a, b, c))
elif a == b - c: print('%d=%d-%d'%(a, b, c))
elif a == b * c: print('%d=%d*%d'%(a, b, c))
elif a == b // c: print('%d=%d/%d'%(a, b, c))
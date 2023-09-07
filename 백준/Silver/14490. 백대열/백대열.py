import sys
import math
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(':'))
print('%d:%d'%(a//math.gcd(a,b), b//math.gcd(a,b)))
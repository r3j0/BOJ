import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
print(math.factorial(n)//60//60//24//7)
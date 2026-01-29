# 30993 : 자동차 주차
import sys
import math
input = sys.stdin.readline

n, a, b, c = map(int, input().rstrip().split())
print(math.comb(n, a) * math.comb(n-a, b))
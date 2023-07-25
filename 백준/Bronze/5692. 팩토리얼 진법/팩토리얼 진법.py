import sys
from math import *
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0': break

    result = 0
    for s in range(len(n)):
        result += (ord(n[s]) - ord('0')) * factorial(len(n)-s)
    
    print(result)
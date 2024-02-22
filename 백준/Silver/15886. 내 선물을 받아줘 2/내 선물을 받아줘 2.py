import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
print(string.count('EW'))
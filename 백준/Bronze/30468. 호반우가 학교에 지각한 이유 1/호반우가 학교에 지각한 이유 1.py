import sys
input = sys.stdin.readline

STR, DEX, INT, LUK, N = map(int, input().rstrip().split())
print(max(((N*4) - (STR + DEX + INT + LUK)), 0))
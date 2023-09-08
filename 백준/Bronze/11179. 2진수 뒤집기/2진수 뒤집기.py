import sys
input = sys.stdin.readline

print(int((bin(int(input()))[2:])[::-1], 2))
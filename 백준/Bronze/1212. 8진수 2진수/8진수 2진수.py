import sys
input = sys.stdin.readline

string = input().rstrip()
print(bin(int(string, 8))[2:])
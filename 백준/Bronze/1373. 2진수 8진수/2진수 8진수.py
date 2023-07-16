import sys
input = sys.stdin.readline

string = input().rstrip()
print(oct(int(string, 2))[2:])
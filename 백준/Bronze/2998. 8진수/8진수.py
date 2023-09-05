import sys
input = sys.stdin.readline

string = input().rstrip()
print(str(oct(int(string, 2)))[2:])
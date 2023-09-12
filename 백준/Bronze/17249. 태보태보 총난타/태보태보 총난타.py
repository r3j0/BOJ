import sys
input = sys.stdin.readline

string = input().rstrip()
left, right = string.split('(^0^)')
print(left.count('@'), right.count('@'))
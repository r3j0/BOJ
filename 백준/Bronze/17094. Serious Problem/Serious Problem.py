import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
if string.count('e') == string.count('2'): print('yee')
else: print('e' if string.count('e') > string.count('2') else '2')
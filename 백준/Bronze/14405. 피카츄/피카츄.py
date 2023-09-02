import sys
input = sys.stdin.readline

string = input().rstrip()
string = string.replace('pi', ' ')
string = string.replace('ka', ' ')
string = string.replace('chu', ' ')
if string.strip() == "": print('YES')
else: print('NO')
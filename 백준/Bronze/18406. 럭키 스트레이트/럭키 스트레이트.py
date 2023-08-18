import sys
input = sys.stdin.readline

string = input().rstrip()
if sum(map(int, list(string[:len(string) // 2]))) == sum(map(int, list(string[len(string) // 2:]))): print('LUCKY')
else: print('READY')
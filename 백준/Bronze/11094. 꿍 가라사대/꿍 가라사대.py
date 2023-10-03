import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    string = input().rstrip()
    if len(string) > 11 and string[:11] == 'Simon says ':
        print(string[10:])
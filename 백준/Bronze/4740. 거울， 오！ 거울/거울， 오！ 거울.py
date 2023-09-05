import sys
input = sys.stdin.readline

while True:
    string = input().rstrip('\n')
    if string == "***": break
    print(string[::-1])
import sys
input = sys.stdin.readline 

while True:
    string = input().rstrip()
    if string[0] == '#': break

    now = string[0]
    string = string[2:].lower()
    print(now, string.count(now))
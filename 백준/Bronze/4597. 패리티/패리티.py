import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '#': break

    if string[-1] == 'e' and string.count('1') % 2 == 0:
        print(string[:-1] + '0')
    elif string[-1] == 'e' and string.count('1') % 2 == 1:
        print(string[:-1] + '1')
    elif string[-1] == 'o' and string.count('1') % 2 == 0:
        print(string[:-1] + '1')
    else:
        print(string[:-1] + '0')
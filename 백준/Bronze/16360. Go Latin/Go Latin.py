import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    if string[-1] == 'a': print(string[:-1] + 'as')
    elif string[-1] == 'i' or string[-1] == 'y': print(string[:-1] + 'ios')
    elif string[-1] == 'l': print(string[:-1] + 'les')
    elif string[-1] == 'n': print(string[:-1] + 'anes')
    elif string[-2:] == 'ne': print(string[:-2] + 'anes')
    elif string[-1] == 'o': print(string[:-1] + 'os')
    elif string[-1] == 'r': print(string[:-1] + 'res')
    elif string[-1] == 't': print(string[:-1] + 'tas')
    elif string[-1] == 'u': print(string[:-1] + 'us')
    elif string[-1] == 'v': print(string[:-1] + 'ves')
    elif string[-1] == 'w': print(string[:-1] + 'was')
    else: print(string + 'us')
import sys
input = sys.stdin.readline

all_string = ""
while True:
    string = ""
    try:
        string = input().rstrip()
    except:
        break

    if string == "": break
    all_string += string

print(sum(list(map(int, all_string.rstrip().split(',')))))
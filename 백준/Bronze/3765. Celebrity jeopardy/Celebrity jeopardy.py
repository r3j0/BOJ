import sys
input = sys.stdin.readline

strings = []
while True:
    try:
        string = input().rstrip()
    except:
        break
    
    if string == "": break
    strings.append(string)

for s in strings: print(s)
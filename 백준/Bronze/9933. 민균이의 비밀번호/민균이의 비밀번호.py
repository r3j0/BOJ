import sys
input = sys.stdin.readline

n = int(input())
finding = {}
finded = ""
for _ in range(n):
    string = input().rstrip()
    if finded != "": continue
    if string[::-1] == string:
        finded = string
    else:
        if not finding.get(string):
            finding[string[::-1]] = 1
        else:
            finded = string

print(len(finded), finded[len(finded)//2])
    
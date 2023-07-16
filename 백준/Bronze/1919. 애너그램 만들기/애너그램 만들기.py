import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
adict = {}
for i in a:
    if adict.get(i): adict[i] += 1
    else: adict[i] = 1
bdict = {}
for i in b:
    if bdict.get(i): bdict[i] += 1
    else: bdict[i] = 1

result = 0
for i in list(adict.keys()):
    if bdict.get(i) and adict[i] != bdict[i]:
        result += abs(adict[i] - bdict[i])
        del adict[i]
        del bdict[i]
    elif (not bdict.get(i)):
        result += adict[i]
        del adict[i]
for i in list(bdict.keys()):
    if adict.get(i) and adict[i] != bdict[i]:
        result += abs(adict[i] - bdict[i])
        del adict[i]
        del bdict[i]
    elif (not adict.get(i)):
        result += bdict[i]
        del bdict[i]

print(result)
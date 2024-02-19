import sys
input = sys.stdin.readline

string = input().rstrip()
arr = []
now = ""
idx = 0
while idx < len(string):
    if string[idx] == ':':
        if now == "":
            if idx > 0 and string[idx-1] == ':':
                arr.append("::")
        else:
            arr.append(now)
            now = ""
    else:
        now += string[idx]
    idx += 1
if now != "":
    arr.append(now)

idx = 0
while idx < len(arr):
    if arr[idx] == '::':
        del arr[idx]
        while len(arr) != 8: arr.insert(idx, '0000')
    else:
        arr[idx] = arr[idx].zfill(4)
    idx += 1

print(':'.join(arr))

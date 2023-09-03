import sys
input = sys.stdin.readline

mode, string = input().rstrip().split()
mode = int(mode)

arr = []
if mode == 1:
    now_str = ""
    for s in string:
        if 'A' <= s <= 'Z':
            arr.append(now_str)
            now_str = s.lower()
        else:
            now_str += s
    arr.append(now_str)
elif mode == 2:
    arr = list(string.split('_'))
else: # mode == 3
    now_str = ""
    for s in string:
        if 'A' <= s <= 'Z' and now_str != "":
            arr.append(now_str)
            now_str = s.lower()
        else:
            now_str += s.lower()
    arr.append(now_str)
    
# 1
for i in range(len(arr)):
    if i == 0: print(arr[0], end='')
    else: print(arr[i][0].upper() + arr[i][1:], end='')

print()

# 2
print('_'.join(arr))

# 3
for i in range(len(arr)):
    print(arr[i][0].upper() + arr[i][1:], end='')

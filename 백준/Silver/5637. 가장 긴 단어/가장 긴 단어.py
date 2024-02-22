import sys
input = sys.stdin.readline

arr = []
cnt = 0
while True:
    try:
        string = input().rstrip()
    except:
        break
    now = ''
    for i in range(len(string)):
        if 'a' <= string[i] <= 'z' or 'A' <= string[i] <= 'Z' or string[i] == '-': now += string[i]
        else:
            if now == '': continue
            else: 
                arr.append([now, cnt])
                cnt += 1
                now = ''
    if now != '':
        arr.append([now, cnt])
        cnt += 1
        if now == 'E-N-D': break
        now = ''
arr.sort(key=lambda x:(-len(x[0]), x[1]))
print(arr[0][0].lower())

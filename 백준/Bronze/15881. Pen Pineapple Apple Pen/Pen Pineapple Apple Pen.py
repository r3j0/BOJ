n = int(input())
string = input()

idx = 3
cnt = 0
while idx < len(string):
    if string[idx-3:idx+1] == 'pPAp':
        idx += 4
        cnt += 1
    else:
        idx += 1
print(cnt)
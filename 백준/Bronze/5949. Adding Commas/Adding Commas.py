import sys
input = sys.stdin.readline

string = input().rstrip()
res = []
cnt = 0
for i in range(len(string)-1, -1, -1):
    res.append(string[i])
    cnt += 1
    if cnt == 3 and i != 0: 
        res.append(',')
        cnt = 0

print(''.join(res[::-1]))
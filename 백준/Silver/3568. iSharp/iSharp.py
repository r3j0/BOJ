import sys
input = sys.stdin.readline

string = input().rstrip()
lis = list(string.split())
arr = []
for i in range(1, len(lis)):
    type = []
    name = []
    for j in range(len(lis[i])-2, -1, -1):
        if 'A' <= lis[i][j] <= 'Z' or 'a' <= lis[i][j] <= 'z': 
            name.append(lis[i][j])
        else:
            type.append(lis[i][j])
    name.reverse()
    for i in range(1, len(type)):
        if type[i] == '[':
            type[i] = ']'
            type[i-1] = '['

    print(lis[0] + ''.join(type) + ' ' + ''.join(name) + ';')
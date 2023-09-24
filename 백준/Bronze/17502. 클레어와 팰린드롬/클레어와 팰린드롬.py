import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = list(input().rstrip())

for i in range(n//2):
    if string[i] == string[-(i+1)] == '?':
        string[i] = 'a'
        string[-(i+1)] = 'a'
    elif string[i] == '?' and string[-(i+1)] != '?':
        string[i] = string[-(i+1)]
    elif string[i] != '?' and string[-(i+1)] == '?':
        string[-(i+1)] = string[i]

if n % 2 == 1: string[n//2] = 'a' if string[n//2] == '?' else string[n//2]

print(''.join(string)) 
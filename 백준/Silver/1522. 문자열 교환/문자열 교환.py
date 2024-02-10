import sys
input = sys.stdin.readline

string = input().rstrip()
b = string.count('b')
result = string[:b].count('a')

for i in range(1, len(string)):
    if i + b <= len(string):
        result = min(result, string[i:i+b].count('a'))
    else:
        result = min(result, string[i:].count('a') + string[:i+b-len(string)].count('a'))

print(result)
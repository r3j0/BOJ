import sys
input = sys.stdin.readline

string = input().rstrip()
min_string = string

for i in range(1, len(string)-1):
    for j in range(i+1, len(string)):
        if min_string == string: min_string = (string[:i])[::-1] + (string[i:j])[::-1] + (string[j:])[::-1]
        else: min_string = min(min_string, (string[:i])[::-1] + (string[i:j])[::-1] + (string[j:])[::-1])

print(min_string)
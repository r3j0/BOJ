import sys
input = sys.stdin.readline

string = input().rstrip()
max_len = 0
for i in range(len(string)):
    for j in range(i, len(string)):
        if string[i:j+1] == string[i:j+1][::-1]: max_len = max(max_len, len(string[i:j+1]))

print(max_len)
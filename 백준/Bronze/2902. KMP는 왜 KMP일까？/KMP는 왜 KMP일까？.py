import sys 
input = sys.stdin.readline

string = input().rstrip()
arr = [string[0]]

for s in range(len(string)):
    if string[s] == '-':
        arr.append(string[s+1])

print(''.join(arr))
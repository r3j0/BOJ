import sys
input = sys.stdin.readline

string = input().rstrip()
done = 0
for length in range(2, len(string)+1, 2):
    for start in range(len(string)-length+1):
        if string[start:start+length] == string[start:start+length][::-1]:
            done = 1
            break
    if done == 1: break

if done == 1: print('Or not.')
else: print('Odd.')
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().strip()
    done = 0
    for s in string:
        if not ('0' <= s <= '9'): 
            done = 1
            break
    
    if done == 1 or string == '': print('invalid input')
    else: print(int(string))
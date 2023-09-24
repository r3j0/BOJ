import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

s_cnt = string.count('s')
t_cnt = string.count('t')

if s_cnt == t_cnt: print(string)
else:
    for i in range(n):
        if string[i] == 's': s_cnt -= 1
        else: t_cnt -= 1

        if s_cnt == t_cnt: 
            print(string[i+1:])
            break
    
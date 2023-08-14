import sys
input = sys.stdin.readline

string = input().rstrip()
arr = []
order = []
idx = 0
nowstring = ""
while idx < len(string):
    if nowstring != "" and (string[idx] == '+' or string[idx] == '-'):
        arr.append(nowstring)
        nowstring = ""
        order.append(string[idx])
    else:
        nowstring += string[idx]
    idx += 1

arr.append(nowstring)

done = 0
for a in range(len(arr)):
    now = arr[a]
    if now == '0': continue
    cnt = 0
    go = 1
    while now[-go] == 'x':
        cnt += 1
        go += 1
    
    if cnt == 0:
        if int(now) == -1:
            print('-', end='')
        elif int(now) != 1:
            print(now, end='')
        print('x', end='')
    else:
        if int(now[:-(go - 1)]) // (cnt + 1) == -1:
            print('-', end='')
        elif int(now[:-(go - 1)]) // (cnt + 1) != 1:
            print(int(now[:-(go - 1)]) // (cnt + 1), end='')
        
        print('x'*(cnt+1), end='')
    done = 1
    
    if a != len(arr) - 1: print(order[a], end='')
if done == 1: print('+', end='')
print('W')
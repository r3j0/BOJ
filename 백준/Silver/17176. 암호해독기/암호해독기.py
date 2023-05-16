import sys
input = sys.stdin.readline

n = int(input().rstrip())
order = list(map(int, input().rstrip().split()))
string = input().rstrip()

def convKey(ch):
    if ch == " ": return 0
    if 'A' <= ch <= 'Z': return ord(ch)-ord('A')+1
    if 'a' <= ch <= 'z': return ord(ch)-ord('a')+27

order_dict = {}
string_dict = {}

for o in order:
    if order_dict.get(o, -1) == -1:
        order_dict[o] = 1
    else:
        order_dict[o] += 1

for s in string:
    now = convKey(s)
    if string_dict.get(now, -1) == -1:
        string_dict[now] = 1
    else:
        string_dict[now] += 1

last = {}
for k, v in order_dict.items():
    if string_dict.get(k, -1) != -1:
        if string_dict[k] == v:
            del string_dict[k]
        else:
            last[k] = v
            break
    else:
        last[k] = v
        break

if len(last) != 0 or len(string_dict) != 0: print('n')
else: print('y')


    

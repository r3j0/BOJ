import sys
input = sys.stdin.readline

first = ''
now = ''
dic = {}
done = 1
for i in range(36):
    s = input().rstrip()
    dic[s] = 1
    if now == '': 
        now = s
        first = s
    else:
        a = abs(ord(now[0]) - ord(s[0]))
        b = abs(ord(now[1]) - ord(s[1]))
        #print(s, now, a, b)
        if (a == 1 and b == 2) or (a == 2 and b == 1): 
            pass
        else:
            done = 0
        now = s
a = abs(ord(now[0]) - ord(first[0]))
b = abs(ord(now[1]) - ord(first[1]))
if (a == 1 and b == 2) or (a == 2 and b == 1): 
    pass
else:
    done = 0

if len(dic) != 36: done = 0
print('Valid' if done == 1 else 'Invalid')
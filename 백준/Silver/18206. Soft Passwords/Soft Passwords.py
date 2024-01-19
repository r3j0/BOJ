p = list(input().rstrip())
s = list(input().rstrip())

def rev(i):
    size = len(i)
    newarr = []
    for a in range(size):
        if 'A' <= i[a] <= 'Z': newarr.append(chr(ord(i[a])+32))
        elif 'a' <= i[a] <= 'z': newarr.append(chr(ord(i[a])-32))
        else: newarr.append(i[a])
    
    return newarr
revp = rev(p)

print('Yes' if ((s == p) or (len(p) == len(s) + 1 and '0' <= p[0] <= '9' and p[1:] == s) or (len(p) == len(s) + 1 and '0' <= p[-1] <= '9' and p[:-1] == s) or (s == revp)) else 'No')
import sys
input = sys.stdin.readline

t = 1
while True:
    string = input().rstrip()
    if string.count('-') > 0: break
    back = 0
    stack = 0
    for i in range(len(string)):
        if string[i] == '{': stack += 1
        else:
            if stack == 0:
                back += 1
            else:
                stack -= 1
    res = (back + 1) // 2 + (stack + 1) // 2

    print('%d. %d'%(t, res))
    t += 1
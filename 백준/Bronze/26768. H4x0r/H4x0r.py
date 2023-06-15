string = list(input().rstrip())
for s in string:
    if s == 'a': print('4', end='')
    elif s == 'e': print('3', end='')
    elif s == 'i': print('1', end='')
    elif s == 'o': print('0', end='')
    elif s == 's': print('5', end='')
    else: print(s, end='')
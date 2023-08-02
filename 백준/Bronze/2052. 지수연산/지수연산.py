a = '%.300f'%(1/(2**int(input())))
a = str(a)
while a:
    if a[-1] == '0':
        a = a[:-1]
    else:
        break
print(a)
import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    num, c = input().rstrip().split()
    if c == 'kg':
        print('%.4f'%(float(num) * 2.2046), 'lb')
    elif c == 'l':
        print('%.4f'%(float(num) * 0.2642), 'g')
    elif c == 'lb':
        print('%.4f'%(float(num) * 0.4536), 'kg')
    else: # g
        print('%.4f'%(float(num) * 3.7854), 'l')
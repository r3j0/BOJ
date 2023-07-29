a = int(input())
b = int(input())
c = int(input())

if min(a, b)/c >= 2 and min(a, b)/max(a, b) <= 2: print('good')
else: print('bad')
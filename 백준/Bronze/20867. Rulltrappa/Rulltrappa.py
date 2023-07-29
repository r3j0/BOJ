m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split()) 

left = 0
if l != 0: left = l/a+(m//g)
else: left = m//g

right = 0
if r != 0: right = r/b+(m//s)
else: right = m//s

if left > right: print('latmask')
elif left < right: print('friskus')

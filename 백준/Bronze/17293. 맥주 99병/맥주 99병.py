import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n, 0, -1):
    print('%d bottle%s of beer on the wall, %d bottle%s of beer.'%(i, 's' if i > 1 else '', i, 's' if i > 1 else ''))
    if i > 1: print('Take one down and pass it around, %d bottle%s of beer on the wall.'%(i-1, 's' if (i-1) > 1 else ''))
    else: print('Take one down and pass it around, no more bottles of beer on the wall.')
    print()

print('No more bottles of beer on the wall, no more bottles of beer.')
print('Go to the store and buy some more, %d bottle%s of beer on the wall.'%(n, 's' if n > 1 else ''))
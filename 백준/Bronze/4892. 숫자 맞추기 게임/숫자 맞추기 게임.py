import sys
input = sys.stdin.readline

t = 1
while True:
    n = int(input().rstrip())
    if n == 0: break
    print('%d.'%(t), 'odd' if (3*n)%2 == 1 else 'even', (n-1)//2 if (3*n)%2 == 1 else n//2)
    t += 1
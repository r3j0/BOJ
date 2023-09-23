import sys
input = sys.stdin.readline

def convertTo(num, k):
    stack = []
    while num > 1:
        stack.append(num % k)
        num //= k
    if num != 0: stack.append(num)
    return ''.join(map(str, stack))

n = int(input().rstrip())

done = 0
for i in range(2, 10):
    now = convertTo(n, i)
    if now == now[::-1]: 
        print(i, now)
        done = 1

if str(n) == str(n)[::-1]:
    print(10, n)
    done = 1

if done == 0: print('NIE')
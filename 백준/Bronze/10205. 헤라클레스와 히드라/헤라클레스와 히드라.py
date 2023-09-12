import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    k = int(input().rstrip())
    string = input().rstrip()

    for s in string:
        if s == 'c': k += 1
        else: k -= 1
    print('Data Set %d:'%i)
    print(k)
    print()
